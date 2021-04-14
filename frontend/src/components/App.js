import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
      };
    }
  
    componentDidMount() {
      fetch("api/schools")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(data => {
          this.setState(() => {
            return {
              data,
              loaded: true
            };
          });
        });
    }

  
    render() {
      return (
          <ul>
               {this.state.loaded && this.state.data.results.map(school => {
                   return (
                       <li key={school.id}>
                           {school.name}
                           <ul>
                               {school.eaterys.map(eatery => {
                                   return (
                                       <li>
                                           {eatery}
                                       </li>
                                   )
                               })}
                           </ul>
                       </li>
                   );
               })}
          </ul>
      );
    }
  }
  
  export default App;
  
  const container = document.getElementById("app");
  render(<App />, container);