# Build for linux
Face verify/comparison python docker project.

<!-- to start -->
docker compose up -d
<!-- to stop -->
docker compose down


- POST http://x.x.x.x:8443/compare
- multipart/form-data
- image_1 => image binary
- image_2 => image binary

