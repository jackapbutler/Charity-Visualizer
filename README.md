# Instructions to Run App
## Prerequisites
Make sure you have **Docker Desktop** and **GitHub Desktop** installed correctly on your local machine.

## Running the App
1.    Clone the Charity-Visualizer repo to your local machine through GitHub Desktop.
2.    Open the command line and **cd** to the directory where Charity-Visualizer is downloaded.
3.    Run the command below to create the docker image from the Dockerfile; <pre> docker build -t charity_app . </pre>
4.    Run the command below to run the application from the Docker image.; <pre> docker run -p 8501:8501 charity_app:latest </pre> 
5.    The app should be available at http://localhost:8501/.
<br/><br/> 
