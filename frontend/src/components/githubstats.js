import React, { useState } from 'react';

function GitHubStats() {
  const [username, setUsername] = useState('');
  const [repos, setRepos] = useState([]);

  const fetchGitHubData = async () => {
    try {
      const response = await fetch(`/api/github/${username}`);
      const data = await response.json();
      setRepos(data);
    } catch (error) {
      console.error('Error fetching GitHub data', error);
    }
  };

  return (
    <div>
      <h3>Enter GitHub Username</h3>
      <input 
        type="text" 
        value={username} 
        onChange={(e) => setUsername(e.target.value)} 
        placeholder="GitHub Username"
      />
      <button onClick={fetchGitHubData}>Fetch Stats</button>

      <div>
        {repos.length > 0 && repos.map(repo => (
          <div key={repo.id}>
            <h4>{repo.name}</h4>
            <p>{repo.description}</p>
            <p>Stars: {repo.stargazers_count}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default GitHubStats;
