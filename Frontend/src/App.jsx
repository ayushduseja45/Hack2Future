// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Navbar from './components/Navbar';
// import Home from './components/Home';
// import Footer from './components/Footer';
// import Conversion from './components/Conversion';
// import ConvertToJPG from './components/ConvertToJPG';
// import StartPage from './components/StartPage';

// function App() {
//   return (
//     <Router>
//       <div>
//         {/* Navbar with links */}
//         <Navbar />

//         {/* Defining Routes */}
//         <Routes>
//           <Route path="/" element={<StartPage />} /> {/* Shows StartPage at root */}
//           <Route path="/home" element={<Home />} /> {/* Navigates to Home page */}
//           <Route path="/convertion" element={<Conversion />} />
//           <Route path="/convert-jpg" element={<ConvertToJPG />} />
//         </Routes>

//         <Footer />
//       </div>
//     </Router>
//   );
// }

// export default App;


import React from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Footer from './components/Footer';
import Conversion from './components/Conversion';
import ConvertToJPG from './components/ConvertToJPG';
import StartPage from './components/StartPage';
import Servillance from './components/Servillance'
// A wrapper component to handle conditional rendering of the Navbar
function Layout() {
  const location = useLocation();

  return (
    <div>
      {/* Conditionally render Navbar */}
      {location.pathname !== '/' && <Navbar />}
      {/* Define the routes */}
      <Routes>
        <Route path="/" element={<StartPage />} />
        <Route path="/home" element={<Home />} />
        <Route path='/upscale' element={<ImageUpload/>}/>
        <Route path='/ser' element={<Servillance/>}/>
        <Route path="/convertion" element={<Conversion />} />
        <Route path="/convert-jpg" element={<ConvertToJPG />} />
        <Route path='/convert_png' element={<ConvertToPNG/>}/>
      </Routes>

      <Footer />
    </div>
  );
}

function App() {
  return (
    <Router>
      <Layout />
    </Router>
  );
}

export default App;

