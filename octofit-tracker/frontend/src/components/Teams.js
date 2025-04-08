import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-header bg-primary text-white">
        <h1>Teams</h1>
      </div>
      <div className="card-body">
        <ul className="list-group">
          {teams.map(team => (
            <li key={team._id} className="list-group-item">
              {team.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Teams;