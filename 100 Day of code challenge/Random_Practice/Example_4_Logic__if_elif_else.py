import os

DEVELOPMENT = 'development'
PRODUCT = 'production'
STAGING = 'staging'
CODE_SPACE = 'code_space'
LOCAL = 'local'

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Developer environment")
elif current_env == PRODUCT:
    print("Product environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env == [CODE_SPACE, LOCAL]:
    print("Code space or Local environment")
else:
    print("Unknown environment")