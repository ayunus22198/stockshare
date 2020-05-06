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
import StockListWrapper from './components/StockListWrapper';
import StockGraphWrapper from './components/StockGraphWrapper';

export default class App extends React.Component {
  
  state = {

  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/" exact component = {StockListWrapper} />
            <Route path="/:stock" exact component = {StockGraphWrapper} />
          </Switch>
        </div>
      </Router>
    );
  }
}

