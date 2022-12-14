## v0.3.0 (2022-12-04)

### Feat

- Added basic prometheus monitoring.
- Moving to Nginx ingress
- Lowered deployment requirements.
- Application can now report its version.
- **ci**: Pushing on the main branch will trigger a build.
- **observability**: Made Kibana optional
- **ci**: Implemented Reusable workflows and composed a deployment pipeline.
- **ci**: Created Helm Chart for deployment

### Fix

- Backend was requesting too many resources.

## v0.1.0 (2022-11-26)

### Feat

- **ci**: Building Twitter-Clone-Docker image.
- **ci**: Skipped installing dependencies
- Created linting workflow.
- Created UserService
- Added Kibana for monitoring.
- Can create and fetch user using the API
- Created and tested user service
- Created DB Simple tweets table.
- Created DB Infrastructure.
- Created Docker image for container.

### Fix

- Formatted project using isort
- Moved workflow to correct folder.
- Imported incorrect datatype in file_blobstore
