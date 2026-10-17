#!/usr/bin/env bash
# PreToolUse(Bash) guard: no commits/pushes on main, no force pushes, no local publishes.
# Publishing to Thunderstore happens only from CI after a PR merges.
INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')
DIR=$(printf '%s' "$INPUT" | jq -r '.cwd // empty')

deny() {
  jq -n --arg r "$1" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
  exit 0
}

# Split on shell separators so "cd x && git push" is still caught.
while IFS= read -r part; do
  part="${part#"${part%%[![:space:]]*}"}"
  case "$part" in
    "tcli publish"*)
      deny "Don't publish locally: merge a PR to main and publish.yml publishes from CI." ;;
    "git push"*)
      case "$part" in
        *" -f"|*" -f "*|*"--force"|*"--force "*|*"--force=*"|*" +"*)
          deny "Force pushes are blocked in this repo. Push a new commit instead." ;;
      esac
      case "$part" in
        *" main"|*" main "*|*":main"*|*" master"*)
          deny "Don't push to main; push a branch and open a PR (main is protected)." ;;
      esac ;;
  esac
  case "$part" in
    "git push"*|"git commit"*)
      [ -n "$DIR" ] && [ -d "$DIR" ] && cd "$DIR"
      BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null)
      if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
        deny "You're on $BRANCH. Create a branch (git switch -c <name>) and commit there; changes reach main via PR."
      fi ;;
  esac
done < <(printf '%s\n' "$CMD" | awk '{gsub(/&&|\|\||;|\|/, "\n"); print}')

exit 0
