// import logo from './logo.svg';
import './App.css';
import { Dashboard } from './components/Dashboard.tsx';
import '@blueprintjs/core/lib/css/blueprint.css';
import '@blueprintjs/table/lib/css/table.css';
import "@blueprintjs/popover2/lib/css/blueprint-popover2.css";

function App() {
  return (
    <div className="App">
      {/*<header className="App-header">*/}
      <header className="Dark-background">
          <Dashboard />
      </header>
    </div>
  );
}

export default App;
