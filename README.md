# cu2m

## Cloning Submodules

Run the following command to clone the two submodules in this repository.

```sh
git submodule update --init
```

## Booting up the Container (Development Profile)

1. Make sure the environment variables are properly set up. Refer to the two submodules for more information.
2. Then run the following command:

```sh
docker compose --profile dev up --build --watch
```

This command should boot up the container given all environment vairables are set correctly. Changes to the files should be reflected immediately in the container.

## Booting up the Container (Production Profile)

1. Make sure the environment variables are properly set up. Refer to the two submodules for more information.
2. Then run the following command:

```sh
docker compose --profile prod up --build --watch
```

This command should boot up the container given all environment vairables are set correctly. Changed files are NOT reflected until a container rebuild.

For other debug information, refer to the submodules for more details.
