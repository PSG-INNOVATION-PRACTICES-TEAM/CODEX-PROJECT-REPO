import './App.css';
import { useState } from 'react';
import Editor from "@monaco-editor/react";
import Navbar from './Components/Navbar';
import Axios from 'axios';
import spinner from './spinner.svg';
const App=()=> {
  const [code, setCode] = useState(``);
  const [lang, setLang] = useState('python');
  const [theme, setTheme] = useState('vs-dark');
  const [fontSize, setFontSize] = useState(20);
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const options = {
    fontSize:fontSize
  }

  function compile() {
    setLoading(true);
    if(code === ``){
      return
    }

    Axios.post(`http://localhost:5000/compile`, {
      code: code,
      language: lang,
      input:input
    }).then((response) => {
      setOutput(response.data.output);
    }).then(() => {
      setLoading(false);
    })
  }

  function clearOutput() {
    setOutput("");
  }

  return (
    <div className="App">
      <Navbar
        lang={lang} setLang={setLang}
        theme={theme} setTheme={setTheme}
        fontSize={fontSize} setFontSize={setFontSize}
      />
      <div className="main">
          <div className="left-container">
            <Editor
                options={options}
                height="calc(100vh-50px)"
                width="100%"
                theme={theme}
                language={lang}
                defaultLanguage="python"
                defaultValue='# Enter Your Code'
                onChange={(value)=> {setCode(value)}}
            />
            <button className="run-btn" onClick={()=>compile()}>
              Run
            </button>
          </div>
          <div className="right-container">
            <h4>Input : </h4>    
            <div className="input-box">
              <textarea id="code-inp" onChange={(e) => { setInput(e.target.value); }}>
              </textarea>
            </div>
            <h4>Output : </h4>
            {loading ? (
              <div className="spinner-box">
                <img src={spinner} alt="Loading..." />
              </div>
              ) :
              (
                <div className="output-box">
                  <pre>{output}</pre>
                  <button onClick={() => { clearOutput() }} className="clear-btn">
                    Clear
                  </button>
                </div>
              )}
          </div>
        </div>
    </div>
  );
}

export default App;

