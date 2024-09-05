document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    fetch(`/api/user/${username}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('userStats').innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                document.getElementById('userStats').innerHTML = `
                    <p><strong>Username:</strong> ${data.login}</p>
                    <p><strong>Name:</strong> ${data.name || 'N/A'}</p>
                    <p><strong>Public Repositories:</strong> ${data.public_repos}</p>
                    <p><strong>Followers:</strong> ${data.followers}</p>
                    <p><strong>Following:</strong> ${data.following}</p>
                    <p><strong>Bio:</strong> ${data.bio || 'N/A'}</p>
                `;
            }
        })
        .catch(error => {
            document.getElementById('userStats').innerHTML = `<p>Error: ${error.message}</p>`;
        });
});
