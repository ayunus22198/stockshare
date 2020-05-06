import React from 'react';
import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";
import StockList from './components/StockList';
import Graphs from './components/Graphs';

export default class App extends React.Component {
  
  state = {

  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/" exact component = {StockList} />
            <Route path="/:stock" exact component = {Graphs} />
          </Switch>
        </div>
      </Router>
    );
  }
}

