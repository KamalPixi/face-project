# Build for linux
- docker build --platform linux/amd64 -t flask-faceproject .
- or docker build -t flask-faceproject .
- docker save -o image_name.tar flask-faceproject
- docker load -i /path/to/destination/image_name.tar
- docker run -p 5000:5000 flask-faceproject


- POST http://139.59.113.219:5000/compare
- multipart/form-data
- image_1 => image binary
- image_2 => image binary

