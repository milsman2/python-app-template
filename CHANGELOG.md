# CHANGELOG

<!-- version list -->

## v1.19.2 (2026-09-06)

### Bug Fixes

- Make release workflow reusable across repos
  ([`176ec0f`](https://github.com/milsman2/python-app-template/commit/176ec0f1f6c518eb83d95ee119b04d3315b32cca))


## v1.19.1 (2026-08-28)

### Bug Fixes

- Modernize GitHub Actions and uv workflows
  ([`25573e1`](https://github.com/milsman2/python-app-template/commit/25573e15cf9463b943f0b2e0f394258a8dd25cb4))

- Update Dockerfile and CI/CD workflow for improved caching and image handling
  ([`eb4f0d1`](https://github.com/milsman2/python-app-template/commit/eb4f0d16999090dbb2d303c5ddf27af6bbece8d0))


## v1.19.0 (2026-03-31)

### Bug Fixes

- Correct platform handling and tag formatting in Docker build workflow
  ([`c76ec11`](https://github.com/milsman2/python-app-template/commit/c76ec11695660a41333d62b5fb520b54f893433a))

- Remove DOCKER_PLATFORMS variable from CI/CD workflow
  ([`551e671`](https://github.com/milsman2/python-app-template/commit/551e671c000033ed36714f7db637501dab7563cc))

- Remove unnecessary blank line in CI/CD workflow
  ([`829fb83`](https://github.com/milsman2/python-app-template/commit/829fb83439f31f6fc7c1dbf83909440afae156f6))

- Update Docker tags format in CI/CD and release workflows
  ([`3158fc0`](https://github.com/milsman2/python-app-template/commit/3158fc03e42b37246582aee7b680abf43e3938a8))

### Features

- Add multi-architecture support for Docker builds and scans
  ([`368b176`](https://github.com/milsman2/python-app-template/commit/368b1768ebca2462ee93c6c96ccb89ebd93463be))

- Add wait step for Docker image availability in build workflow
  ([`b08fdef`](https://github.com/milsman2/python-app-template/commit/b08fdef0a9dcab51614456e43b1c9bd0ada689bd))

- Simplify Docker build workflow by removing unused variables and updating multi-arch image handling
  ([`103a0af`](https://github.com/milsman2/python-app-template/commit/103a0afe8db8c85f6337d09d46ac59df852d7d65))


## v1.18.2 (2026-03-28)

### Bug Fixes

- Formatting and settings management
  ([`f708de5`](https://github.com/milsman2/python-app-template/commit/f708de5059cf04811e35871b7829a38274ba2127))


## v1.18.1 (2026-03-27)

### Bug Fixes

- Update workflow references to use main branch and add black configuration
  ([`dfda970`](https://github.com/milsman2/python-app-template/commit/dfda97077ec0b1c042359bfe1a750ea4d5235ca5))


## v1.18.0 (2026-03-27)

### Features

- Update workflows
  ([`99f305b`](https://github.com/milsman2/python-app-template/commit/99f305b61fa96c00cf0f92a72e004983e9726570))


## v1.17.4 (2026-03-22)

### Bug Fixes

- Implement multiple code changes to enhance functionality and improve performance
  ([`66dc99e`](https://github.com/milsman2/python-app-template/commit/66dc99ee483cf8d9c6f375e8fe843470c3443ac1))


## v1.17.3 (2026-03-20)

### Bug Fixes

- Refactor data loading services and update dependencies
  ([`5e719eb`](https://github.com/milsman2/python-app-template/commit/5e719eb1b406002e69bc0d2db9f4f930755ecfa2))

- Update test for logger normal mode to use loguru directly
  ([`6daa1fc`](https://github.com/milsman2/python-app-template/commit/6daa1fc6d07f62339d13d7c6868c8091d1567592))


## v1.17.2 (2026-03-08)

### Bug Fixes

- Standardize logging across the application and improve metric handling
  ([`275cfe0`](https://github.com/milsman2/python-app-template/commit/275cfe02604dd8c63799431974c8889933cb12ec))


## v1.17.1 (2026-03-07)

### Bug Fixes

- Clean up logging and metrics handling across the application
  ([`37b12a0`](https://github.com/milsman2/python-app-template/commit/37b12a0d66b381fee1c8f12122ad830469b56742))


## v1.17.0 (2026-03-04)

### Features

- Enhance display function with logging and summary of astronomical events
  ([`8480bb9`](https://github.com/milsman2/python-app-template/commit/8480bb952537415b963bd6d251cdd8de3b0b60dc))

- Refactor HTTP client usage and remove auto-merge workflow
  ([`2678d77`](https://github.com/milsman2/python-app-template/commit/2678d7746f8f827913b822310e861102efbe5bc9))


## v1.16.0 (2026-03-04)

### Features

- Update dependencies and refactor UI components for astronomical data display
  ([`3c865fa`](https://github.com/milsman2/python-app-template/commit/3c865fa5f85ebe14ee5025d25a11d9b1a54fdd64))


## v1.15.0 (2026-03-02)

### Features

- Enhance astronomical data fetching and display with hourly forecast
  ([`320f73b`](https://github.com/milsman2/python-app-template/commit/320f73b3aa327f400f8af399c0f925e2039d99b0))


## v1.14.1 (2026-02-27)

### Bug Fixes

- Add permissions for auto-merge job to allow write access to pull requests
  ([`6574e36`](https://github.com/milsman2/python-app-template/commit/6574e36a147c30f930e1ea4c9d1cf50458d9e280))

- Rename workflow and simplify head_branch handling in auto-merge script
  ([`648094d`](https://github.com/milsman2/python-app-template/commit/648094dae9b220177adfef98d9f09e25299516b8))

- Update dependencies for ruff and uv to latest versions
  ([`1cc033e`](https://github.com/milsman2/python-app-template/commit/1cc033e1e529a2eaa23d6accace0de01e727f5e7))

- Update scheduler to fetch data every 5 minutes instead of 24 hours
  ([`28d14f7`](https://github.com/milsman2/python-app-template/commit/28d14f76f54ee51e8a4e80c571e9710c9667fcdc))


## v1.14.0 (2026-02-27)

### Bug Fixes

- Update dependencies
  ([`6d75cf8`](https://github.com/milsman2/python-app-template/commit/6d75cf8f6e62a41bc7bf909d3dc5ddd311990f04))

### Features

- Add run_checks script and improve scheduling logic for display
  ([`d03dbc8`](https://github.com/milsman2/python-app-template/commit/d03dbc8c0884d0f525bfa86faaeeb6aceb322ded))

- Refactor astronomical data fetching and display logic
  ([`55d92e8`](https://github.com/milsman2/python-app-template/commit/55d92e8817457378ef1bb1ae0eef20c5298986df))


## v1.13.0 (2026-02-23)

### Features

- Add Docker support with docker-compose and Prometheus integration
  ([`8fb03ae`](https://github.com/milsman2/python-app-template/commit/8fb03aeabad5384e6919c2e407707f114a914405))

### Refactoring

- Reorganize import statements in config.py
  ([`710a0b7`](https://github.com/milsman2/python-app-template/commit/710a0b7bf2b3c8311f4df380fe1256b541d90235))


## v1.12.0 (2026-02-19)

### Chores

- Update Trivy action to v0.34.0 and bump pydantic-settings version to 2.13.0
  ([`50e2749`](https://github.com/milsman2/python-app-template/commit/50e2749338acd3f76118cc991ddfcc86aa105222))

### Features

- Refactor application structure and integrate Prometheus metrics
  ([`041018a`](https://github.com/milsman2/python-app-template/commit/041018a28976b48a0c7a88720740d6c28506319d))


## v1.11.1 (2026-02-14)

### Bug Fixes

- Reorganize service layer and move data loading logic to separate module
  ([`ae235a4`](https://github.com/milsman2/python-app-template/commit/ae235a4059b8e1788b09b46a70ae75cbe2129f9c))


## v1.11.0 (2026-02-14)

### Bug Fixes

- Update job dependencies in CI/CD workflow for proper execution order
  ([`b88538d`](https://github.com/milsman2/python-app-template/commit/b88538d13731b03290281953a56501e986020b10))

### Chores

- Remove obsolete run-branch-scan workflow file
  ([`fc68211`](https://github.com/milsman2/python-app-template/commit/fc68211a5008b5b22707522603c191fff48ee03f))

### Features

- Refactor CI/CD workflows and enhance synthwave UI for astronomical data display
  ([`aa3532b`](https://github.com/milsman2/python-app-template/commit/aa3532b5e74839a93838af5f9ee740e79ee0ea90))

### Refactoring

- Remove redundant import of setup_logger in core modules
  ([`800e8ac`](https://github.com/milsman2/python-app-template/commit/800e8acfde7cc429987590a4d13d5c4d7aefe207))


## v1.10.0 (2026-02-14)

### Bug Fixes

- Add logging for input coordinates in run_app function
  ([`c5bb322`](https://github.com/milsman2/python-app-template/commit/c5bb3225a1f1cd516fc14c41f73f96249c54af65))

- Remove unused imports from display.py
  ([`874aa35`](https://github.com/milsman2/python-app-template/commit/874aa3574ce265179b6b04f1146dda39ea4f0a22))

- Update CI/CD workflows to ensure proper execution conditions for Docker and Trivy scan
  ([`ecd46f1`](https://github.com/milsman2/python-app-template/commit/ecd46f1889ff265faddf330a5c6e3b8caaebff64))

### Features

- Implement CI/CD pipeline with linting, testing, and release workflows; enhance display
  functionality with rich formatting
  ([`5590ee9`](https://github.com/milsman2/python-app-template/commit/5590ee922c9ada56aad2131d3865f60a4d3665e1))


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
