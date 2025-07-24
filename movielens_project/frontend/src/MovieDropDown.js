import React from "react";

const MovieDropdown = ({ movies, onSelect }) => {
  return (
    <select onChange={(e) => onSelect(movies[e.target.value])}>
      <option value="">Select a Movie</option>
      {movies.map((movie, index) => (
        <option key={index} value={index}>
          {movie.title}
        </option>
      ))}
    </select>
  );
};

export default MovieDropdown;
