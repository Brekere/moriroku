function loadJSFilePrinter(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/BrowserPrint-3.0.216.min.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);

    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/BrowserPrint-Zebra-1.0.216.min.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);

    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/zebra_printer/format_connection.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
  }

function loadJSFile(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/scanner_connection/scanner.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
}

function loadImproveJSFile(){
    var scriptTag = document.createElement("script");
    scriptTag.setAttribute("type", "text/javascript");
    scriptTag.setAttribute("src", "/static/js/scanner_connection/scanner_improved.js");
  
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(scriptTag);
}