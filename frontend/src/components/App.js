import './App.css';
import School from './School'
import { useState, useEffect } from 'react';

function App() {

  const [schools, setSchools] = useState([])

  const getSchools = async () => {
    const response = await fetch(`https://ratemydininghall.herokuapp.com/api/schools`)
    const data = await response.results
    setSchools(data)
  }

  useEffect(()=>{
    getSchools()
  },[])

  return (
    <div className="App">
      {schools.map(school => {
        <School name={school.name}/>
      })}
    </div>
  );
}

export default App;
  
const container = document.getElementById("app");
render(<App />, container);