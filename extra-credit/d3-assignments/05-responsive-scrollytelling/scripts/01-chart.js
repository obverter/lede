(function() {
  const margin = {
  top: 30,
  right: 20,
  bottom: 30,
  left: 50
}

const width = 700 - margin.left - margin.right
const height = 400 - margin.top - margin.bottom

const svg = d3
  .select('#chart-1')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

const xPositionScale = d3.scaleBand().range([0, width])

const yPositionScale = d3
  .scaleLinear()
  .domain([0, 85])
  .range([height, 0])

const colorScale = d3
  .scaleOrdinal()
  .range([
    '#8dd3c7',
    '#ffffb3',
    '#bebada',
    '#fb8072',
    '#80b1d3',
    '#fdb462',
    '#b3de69'
  ])

d3.csv('data/countries.csv').then(ready)

function ready(datapoints) {
  // Sort the countries from low to high
  datapoints = datapoints.sort((a, b) => {
    return a.life_expectancy - b.life_expectancy
  })

  // And set up the domain of the xPositionScale
  // using the read-in data
  const countries = datapoints.map(d => d.country)
  xPositionScale.domain(countries)

  /* Add your rectangles here */

  d3.select('#asia-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', 'lightgrey')
    svg.selectAll('.asia').attr('fill', '#4cc1fc')
  })

  d3.select('#africa-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', 'lightgrey')
    svg.selectAll('.africa').attr('fill', '#4cc1fc')
  })

  d3.select('#na-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', 'lightgrey')
    svg.selectAll('.namerica').attr('fill', '#4cc1fc')
  })

  d3.select('#low-gdp-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', d => {
      if (d.gdp_per_capita < 3000) {
        return '#4cc1fc'
      } else {
        return 'lightgrey'
      }
    })
  })

  d3.select('#continent-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', d => {
      return colorScale(d.continent)
    })
  })

  d3.select('#reset-btn').on('click', () => {
    svg.selectAll('rect').attr('fill', 'lightgrey')
  })

  svg
    .selectAll('rect')
    .data(datapoints)
    .enter()
    .append('rect')
    .attr('width', xPositionScale.bandwidth())
    .attr('height', d => {
      return height - yPositionScale(d.life_expectancy)
    })
    .attr('x', d => {
      return xPositionScale(d.country)
    })
    .attr('y', d => {
      return yPositionScale(d.life_expectancy)
    })
    .attr('fill', 'lightgrey')
    .attr('class', d => {
      return d.continent.toLowerCase().replace(/[^a-z]*/g, '')
    })

  svg.append('text')
    .text('higher GDP ⟶')
    .attr('class', 'gdp-note')
    .attr('text-anchor', 'middle')
    .attr('font-size', 12)
    .attr('x', width * 0.75)
    .attr('y', height + 15)

  svg.append('text')
    .text('⟵ lower GDP')
    .attr('class', 'gdp-note')
    .attr('text-anchor', 'middle')
    .attr('font-size', 12)
    .attr('x', width * 0.25)
    .attr('y', height + 15)

  const yAxis = d3
    .axisLeft(yPositionScale)
    .tickSize(-width)
    .ticks(5)
    .tickFormat(d => d === 80 ? '80 years' : d)

  svg
    .append('g')
    .attr('class', 'axis y-axis')
    .call(yAxis)
    .lower()

  d3.select('.y-axis .domain').remove()
}
})()