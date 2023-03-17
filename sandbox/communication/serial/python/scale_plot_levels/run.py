from web import app 

print(app.url_map)

app.run(debug=True, host='0.0.0.0', port=5010)