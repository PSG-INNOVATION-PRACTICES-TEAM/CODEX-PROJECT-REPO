import React from 'react'
import Select from 'react-select';
import '../Styles/Navbar.css';


const Navbar= ({lang,setLang,theme,setTheme,fontSize,setFontSize}) => {
    const Languages = [
        { value: 'c', label: "C" },
        { value: 'cpp', label: "C++" },
        { value: 'java', label: "Java" },      
        { value: 'python', label: "Python" }
    ];
    const Themes = [
        { value: 'vs-dark', label: 'Dark' },
        { value: 'light', label: 'Light' }
    ];
    return (
        <div className="navbar">
            <h1>CODEX Code Editor</h1>
            <Select options={Languages} value={lang}
                onChange={(e) => setLang(e.value)}
                placeholder={lang} />
            <Select options={Themes} value={theme}
                onChange={(e) => setTheme(e.value)}
                placeholder={theme} />
            <label>Font Size</label>
            <input type="range" min="18" max="30"
                value={fontSize} step="2"
                onChange={(e) => {setFontSize(e.target.value)}} />
        </div>
    )
}

export default Navbar