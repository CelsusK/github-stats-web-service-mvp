Github Stats Web Service
Authors:
 Kingson Bundi – LinkedIn : https://www.linkedin.com/in/Kingson Mwai
    Albert Gitari – LinkedIn : https://www.linkedin.com/in/Albert
    Cassian Celsus – LinkedIn : https://www.linkedin.com/in/cassian-kiragu-590120263

Introduction

Git Stats Web Service is a comprehensive tool designed to visualize and analyze GitHub repository and user statistics. In a world where code is the heart of innovation, GitHub serves as a powerful platform for developers to collaborate, contribute, and grow. With Git Stats Web Service, users can track critical data points such as commit history, language distribution, pull request statistics, and much more—all presented in an intuitive, user-friendly interface.

This service was born out of a personal need to better understand and showcase our contributions and work. Often, great work happens behind the scenes, and this project aims to bring that to the forefront for developers and teams alike.

Project Blog: Final Blog Post
https://docs.google.com/document/d/1dNkxDRbSJzKa6hXZkqacP9dat3Rqryz-NL86Rip1AD0/edit?usp=sharing

Installation
To run the Git Stats Web Service locally, follow these steps:
Clone the repository:
  bash
git clone https://github.com/your-username/git-stats-webservice.git
Navigate to the project directory:
bash
cd git-stats-web service
Install the required dependencies:
bash
npm install
Create an .env file in the project root directory and add your GitHub API key:
env
GITHUB_API_KEY=your_api_key_here

Run the application:
bash
 npm start
 Visit http://localhost:3000 in your browser to explore the Git Stats Web Service!


Usage
Once you have the application up and running, you can use it to search for a GitHub username or repository. The app will then display detailed statistics, including:
 Commit History: A graphical breakdown of the commits over time.
  Contributors: List of all contributors and their contribution stats.
   Language Usage: The percentage of code in different programming languages.
  Pull Requests & Issues: Insights into open/closed pull requests and issues.
Example Screenshot:
Git Stats Web Service Screenshot

 Contributing
We believe collaboration makes everything better. Contributions to the Git Stats Web Service are more than welcome! Here's how you can get involved:
 Fork the repository.
Create a new feature branch:
bash
git checkout -b feature-name
Make your changes and commit them:
bash
git commit -m "Add feature description"

Push the changes to your branch:
bash
git push origin feature-name
 Open a Pull Request and describe the changes you’ve made.
Once your pull request is reviewed and accepted, it will be merged into the main branch!
Licensing
This project is licensed under the MIT License. Please see the LICENSE file for more details.https://docs.google.com/document/d/1haeqqxc-gyfMcriiCjU2PAG-aGcWH7_eUrbEZgLeA8w/edit?usp=sharing
 You're free to use, modify, and distribute this project, but we kindly ask that you credit the original authors.
Technical Insights & Project Story
The Problem We Set Out to Solve
The idea for Git Stats Web Service stemmed from a personal challenge: How do we quantify and visualize the work we put into open-source projects? GitHub provides raw data, but the lack of an intuitive, engaging interface made us realize there was room for improvement.
As developers, we often find ourselves diving into repositories, analyzing our own or others' contributions. But we felt there was a gap in how easily this data could be accessed and understood. That's where this project was born—to make GitHub statistics accessible and digestible for all developers, whether they're part of a team or working solo.
Technical Challenges We Overcame
GitHub API Rate Limiting: One of the earliest challenges was dealing with the rate limits of the GitHub API. Initially, we found ourselves locked out quickly during development. This pushed us to implement caching mechanisms and optimize how we made API calls, making the app more efficient.
Data Visualization: Presenting the data in a way that’s both visually appealing and informative was another hurdle. We used Chart.js for the graphical representation of commits and language breakdowns. Experimenting with different visualizations, we aimed to strike a balance between beauty and clarity.
Handling Large Repositories: For users analyzing repositories with extensive histories, performance became an issue. We implemented lazy loading for certain components and carefully managed state to ensure the app remained snappy, even with large datasets.

This is only the beginning. In future versions, we hope to expand features to include:
   Traffic Analysis: Gain insights into the number of views and clones for    each repository.
   Detailed User Contributions: Allow users to deep dive into specific areas like code reviews, issue comments, and more.
   Team Collaboration: Add a feature for teams to visualize group contributions to multiple repositories in one dashboard.

The Human Side of the Journey
Throughout the development of Git Stats Web Service, we faced both technical and personal challenges. Late nights debugging caching issues, moments of frustration when the visualizations didn’t quite click, and the joy of finally seeing everything come together—all of it was part of our journey. This project isn't just about stats; it's about growth, learning, and perseverance.
As developers, we understand the importance of community and feedback. This app is as much a reflection of the open-source ethos as it is of our journey as developers. We hope this tool helps others showcase their contributions with pride.
Let’s build and grow together, one commit at a time.
