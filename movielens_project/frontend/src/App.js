import React, { useState } from "react";
import MovieDropdown from "./MovieDropDown";
import topMovies from "./top10.json";

function App() {
  const [selectedMovie, setSelectedMovie] = useState(null);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h2>🎬 Top 10 Movie Dropdown</h2>
      <MovieDropdown movies={topMovies} onSelect={setSelectedMovie} />

      {selectedMovie && (
        <div style={{ marginTop: "20px" }}>
          <h3>{selectedMovie.title}</h3>
          <p><strong>Average Rating:</strong> {selectedMovie.avg_rating}</p>
          <p><strong>Rank:</strong> #{selectedMovie.rank}</p>
          <p><strong>Genres:</strong> {selectedMovie.genres}</p>
          <p><strong>Number of Ratings:</strong> {selectedMovie.num_ratings}</p>
        </div>
      )}
    </div>
  );
}

export default App;
