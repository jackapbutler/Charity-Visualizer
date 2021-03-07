# Instructions to Run App
## Prerequisites
Make sure you have **Docker Desktop** and **GitHub Desktop** installed correctly on your local machine.

## Running the App
<pre>
1.    Clone the Charity-Visualizer repo to your local machine through GitHub Desktop.
2.    Open the command line and **cd** to the directory where Charity-Visualizer is downloaded.
3.    Run the command; **docker build -t charity_app .** to create the docker image from the Dockerfile.
4.    Run the command; **docker run -p 8501:8501 charity_app:latest** to run the application from the Docker image.
5.    The app **should** be available at http://localhost:8501/.
</pre>
<br/><br/> 

# Future Ambitions:
Aims to accurately allocate large charitable contributions to the organisations that deserve it the most. Use reinforcement learning to optimise world humanity wellbeing statistics based on allocation of money to charities. Include “AI-Powered High Impact Fund” based on criteria which uses machine learning to optimise portfolio. Which donates monthly to predicted causes and charities within those causes. Use [data.gov.ie](http://data.gov.ie/) for society wellbeing statistics, etc. Also [worldbank.com](http://worldbank.com/) and other websites.
<br/><br/> 

Research how to identify important causes:
- Criteria can be % change over last X period (example increase in homelessness)
- Cost related values based on increases.
- Using auto-time series to predict which causes will increase the most.
<br/><br/> 

Research how to identify which charity deserves investment: 
- Criteria can be % on budget on admin/overhead (maybe in Irish data)
- Cost effectiveness for each dollar (givewell)
- Financial/Other transparency metrics (charity navigator)
<br/><br/> 
