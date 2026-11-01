def load_env(path=".env"):
    env = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()

    return env