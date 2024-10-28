dir := "./Forritun1/skilaverkefni/skilaverkefni5/"

# dir := "./Forritun1/" # path for testing.py

run *args:
    #!/bin/bash
    (
        cd {{dir}};
        python {{args}};
    )

sync msg:
    #!/bin/bash
    set -euo pipefail
    git add .
    git commit -m '{{msg}}'
    git pull origin main
    git push origin main

push msg:
    git add .
    git commit -m '{{msg}}'
    git push origin main

pull:
    git pull origin main

#[no-cd]
# pytest:
#     python -m # command to run