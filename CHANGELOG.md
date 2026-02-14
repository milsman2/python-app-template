# CHANGELOG

<!-- version list -->

## v1.9.1 (2026-02-14)

### Bug Fixes

- Simplify logger configuration by removing unnecessary lambda functions
  ([`f0f5276`](https://github.com/milsman2/python-app-template/commit/f0f52767908a2dcbc8038b8b03a2206f996c7d46))


## v1.9.0 (2026-02-14)

### Bug Fixes

- Add sample weather data JSON for location and time information
  ([`4e7a960`](https://github.com/milsman2/python-app-template/commit/4e7a9607cdd0c2b1121dec37b9da9a45db53f7a1))

### Features

- Add Ruff linting workflow and update dependencies for improved code quality
  ([`56cfe3a`](https://github.com/milsman2/python-app-template/commit/56cfe3ace5f9204816a0db641d86efbd1c960262))


## v1.8.0 (2026-02-13)

### Bug Fixes

- Add docstring to test_config.py for improved clarity on test coverage
  ([`f04f4d5`](https://github.com/milsman2/python-app-template/commit/f04f4d5560db7729eedaba02f420b41a381417b6))

### Features

- Add pydantic-extra-types for enhanced coordinate handling and update weather settings
  ([`90804bd`](https://github.com/milsman2/python-app-template/commit/90804bd9557fcec60020ef89fbee787224ca39d6))


## v1.7.0 (2026-02-12)

### Bug Fixes

- Refactor imports and enhance data fetching for astronomical data display
  ([`3131aa2`](https://github.com/milsman2/python-app-template/commit/3131aa282ad7b5e060ff258b5f2c83dbbb584c41))

### Features

- Implement weather.gov astronomical data fetching and display
  ([`021c397`](https://github.com/milsman2/python-app-template/commit/021c3973a22c5589e585ddc91f2659b5cde39c87))


## v1.6.0 (2026-02-11)

### Bug Fixes

- Add DOCKER_PUSH_BOOL input to Docker workflow for conditional image pushing
  ([`9743034`](https://github.com/milsman2/python-app-template/commit/97430345a45a9029bdd07c386b1fea92e3d0e938))

- Update actions/checkout version and change username reference to vars in Docker workflow
  ([`4e53c54`](https://github.com/milsman2/python-app-template/commit/4e53c5466e79dddfe91ad7fb3d71a8a4502d3f1f))

- Update Docker tags to remove repository prefix in branch scan workflow
  ([`7f5177c`](https://github.com/milsman2/python-app-template/commit/7f5177cfd08be8ec87bb6d832254d0f2bcb8150e))

- Update uv to 0.10.2
  ([`1f64d5a`](https://github.com/milsman2/python-app-template/commit/1f64d5ad23f311acb02afee9da0bde7388784092))

- Update UV_VERSION to 0.10.2 in workflow files
  ([`a4f71c9`](https://github.com/milsman2/python-app-template/commit/a4f71c9912d84daf046fb80b59fb36fce17d1069))

### Features

- Add Docker-Release job to workflow for building and pushing Docker images
  ([`e86881d`](https://github.com/milsman2/python-app-template/commit/e86881de56105844b2b5db651fbe953a7f434cd6))

- Streamline Docker workflow by removing unnecessary inputs and adding branch scan workflow
  ([`b29c79b`](https://github.com/milsman2/python-app-template/commit/b29c79b5f1249cbb87d6a4635b20a3a3efe02a9a))

- Update Docker workflow to include optional load boolean for image build
  ([`04fa14d`](https://github.com/milsman2/python-app-template/commit/04fa14d7348a51ea6daf1c45dbd5f3bd9b0b7e56))


## v1.5.0 (2026-02-07)

### Features

- Update Docker workflow to include DockerHub login and adjust image tagging
  ([`f7a2866`](https://github.com/milsman2/python-app-template/commit/f7a286649cbc2d43dd036d8912efabae545ec37a))


## v1.4.0 (2026-02-07)

### Features

- Enhance logging setup and add rich output support with figlet
  ([`382616b`](https://github.com/milsman2/python-app-template/commit/382616b535ada89f0b6f42276b8ae791e888591c))


## v1.3.0 (2026-02-07)

### Features

- Add workflow_call inputs for Docker build and scan
  ([`987a2b1`](https://github.com/milsman2/python-app-template/commit/987a2b1f91583e4e04b1c3cd47686a0a69c50859))

- Docker release workflow integration and branch setup
  ([`5b288c9`](https://github.com/milsman2/python-app-template/commit/5b288c9e83c0fa89e9e23d0ba649f802b2a58658))


## v1.2.0 (2026-02-04)

### Bug Fixes

- Downgrade actions and setup versions in Docker workflow
  ([`4f8fa56`](https://github.com/milsman2/python-app-template/commit/4f8fa5682153cfd2b42cca8c2e7c36f1cd9cceb0))

- Normalize environment variable names in Docker workflow
  ([`fb708d9`](https://github.com/milsman2/python-app-template/commit/fb708d948574eabaa427969dca223c2c13e06b03))

- Normalize formatting of environment variables in Docker workflow
  ([`7c0b3f7`](https://github.com/milsman2/python-app-template/commit/7c0b3f73ef6cf4455c80814c067251b30ef0317f))

- Reorder steps in Docker workflow and update image reference for Trivy scan
  ([`5fff51d`](https://github.com/milsman2/python-app-template/commit/5fff51d4090568437a2ce6c0603dc05a5ffa227b))

### Features

- Add Dockerfile and GitHub Actions workflow for Docker build and Trivy scan
  ([`2db6f30`](https://github.com/milsman2/python-app-template/commit/2db6f30a195a3d9bdd19018bc8bc50560616cfd5))


## v1.1.4 (2026-02-02)

### Bug Fixes

- Bump astral-sh/setup-uv from 6 to 7
  ([`a057804`](https://github.com/milsman2/python-app-template/commit/a0578049262cd060fd50c160805db78bd3d51d18))


## v1.1.3 (2026-02-02)

### Bug Fixes

- Bump actions/checkout from 4 to 6
  ([`8462ff8`](https://github.com/milsman2/python-app-template/commit/8462ff8d95045e251b6642a4635851526956e600))


## v1.1.2 (2026-02-02)

### Bug Fixes

- Bump actions/cache from 4 to 5
  ([`9ef9827`](https://github.com/milsman2/python-app-template/commit/9ef98271da933c7802834ee2d457ddb4b423bc9d))


## v1.1.1 (2026-02-02)

### Bug Fixes

- Update branch filter and cache key for UV build workflow
  ([`52a1297`](https://github.com/milsman2/python-app-template/commit/52a1297ed63bbd335322a256aa8351989c112617))


## v1.1.0 (2026-02-02)

### Features

- Add dependabot configuration and update dependencies including httpx
  ([`5ca09d9`](https://github.com/milsman2/python-app-template/commit/5ca09d9b0a2f1d222b2fd8c907ef6038cc0cd3fe))


## v1.0.0 (2026-01-31)

- Initial Release
