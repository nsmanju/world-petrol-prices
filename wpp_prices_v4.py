import plotly.graph_objects as go

data = {
    '🇱🇧 Lebanon': 6.11,
    '🇭🇰 Hong Kong': 2.96,
    '🇸🇬 Singapore': 2.74,
    '🇮🇸 Iceland': 2.39,
    '🇩🇰 Denmark': 2.3,
    '🇫🇷 France': 2.2,
    '🇮🇹 Italy': 2.16,
    '🇳🇱 Netherlands': 2.16,
    '🇫🇮 Finland': 2.15,
    '🇬🇷 Greece': 2.13,
    '🇳🇴 Norway': 2.13,
    '🇩🇪 Germany': 2.02,
    '🇸🇪 Sweden': 2.01,
    '🇧🇪 Belgium': 2,
    '🇨🇭 Switzerland': 1.95,
    '🇬🇧 UK': 1.83,
    '🇦🇹 Austria': 1.82,
    '🇪🇸 Spain': 1.82,
    '🇵🇱 Poland': 1.63,
    '🇹🇷 Turkey': 1.46,
    '🇦🇺 Australia': 1.27,
    '🇯🇵 Japan': 1.26,
    '🇿🇦 South Africa': 1.25,
    '🇰🇷 South Korea': 1.24,
    '🇨🇦 Canada': 1.21,
    '🇲🇽 Mexico': 1.21,
    '🇮🇳 India': 1.18,
    '🇧🇷 Brazil': 1.09,
    '🇵🇰 Pakistan': 0.99,
    '🇨🇳 China': 0.95,
    '🇺🇸 USA': 0.95,
    '🇦🇷 Argentina': 0.8,
    '🇦🇪 UAE': 0.79,
    '🇮🇩 Indonesia': 0.67,
    '🇷🇺 Russia': 0.63,
    '🇸🇦 Saudi Arabia': 0.62,
    '🇳🇬 Nigeria': 0.57,
    '🇮🇷 Iran': 0.36,
    '🇪🇬 Egypt': 0.33,
    '🇰🇼 Kuwait': 0.28,
    '🇻🇪 Venezuela': 0.02
}

countries = list(data.keys())
petrol_price = list(data.values())

# Create the logarithmic horizontal bar chart
fig = go.Figure(data=[go.Bar(
    x=petrol_price,
    y=countries,
    orientation='h',
    marker_color='rgb(124, 166, 202)',
    text=[f'${price:.2f}' for price in petrol_price],
    textposition='outside',
    textfont=dict(size=25,color='red'),
    insidetextfont=dict(size=14),
    hoverinfo='none'
)])

fig.update_layout(
    title='Petrol Price by Country',
    xaxis_title='Petrol Price (log scale)',
    yaxis_title='Country',
    xaxis_type='log',
    #textfont= (size=20),
    template='plotly_white'
)

# Show the plot
fig.show()
