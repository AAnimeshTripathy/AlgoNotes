import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold text-xl">AlgoNotes</div>
        <div className="space-x-4">
          <Link to="/" className="text-white">Home</Link>
          <Link to="/subjects" className="text-white">Subjects</Link>
          <Link to="/bookmarks" className="text-white">Bookmarks</Link>
          <Link to="/blogs" className="text-white">Blogs</Link>
          <Link to="/todo" className="text-white">Todo</Link>
          <Link to="/about" className="text-white">About Us</Link>
          <Link to="/contact" className="text-white">Contact Us</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
