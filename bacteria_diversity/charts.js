function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("samples.json").then((data) => {
    var sampleNames = data.names;

    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    var firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

// Initialize the dashboard
init();

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildMetadata(newSample);
  buildCharts(newSample);
  
}

// Demographics Panel 
function buildMetadata(sample) {
  d3.json("samples.json").then((data) => {
    var metadata = data.metadata;
    // Filter the data for the object with the desired sample number
    var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
    var result = resultArray[0];
   
    // Use d3 to select the panel with id of `#sample-metadata`
    var PANEL = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    PANEL.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });

  });
}

// Deliverable 1: 1. Create the buildChart function.
function buildCharts(sample) {
  // Deliverable 1: 2. Use d3.json to load the samples.json file 
  d3.json("samples.json").then((data) => {
    //console.log(data);

    // Deliverable 1: 3. Create a variable that holds the samples array. 
    let samples = data.samples
    //console.log(samples)

    // Deliverable 1: 4. Create a variable that filters the samples for the object with the desired sample number.
    console.log(sample)
    let selected = samples.filter(entry => entry.id == sample)[0]
    //console.log(selected)

    // Deliverable 3: 1. Create a variable that filters the metadata array for the object with the desired sample number.
    let metadata = data.metadata.filter(entry => entry.id == sample)[0]
    console.log(metadata)

    // Deliverable 1: 5. Create a variable that holds the first sample in the array.
    // already done

    // Deliverable 3: 2. Create a variable that holds the first sample in the metadata array.
    // already done

    // Deliverable 1: 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
    otu_ids = selected.otu_ids
    otu_labels = selected.otu_labels
    sample_values = selected.sample_values
    array_of_objects = []

    for (let i=0; i<otu_ids.length; i++) {
      array_of_objects.push({
        id: otu_ids[i],
        label: otu_labels[i],
        value: sample_values[i]
      })
    }

    console.log(array_of_objects)

    // Deliverable 3: 3. Create a variable that holds the washing frequency.
    wfreq = parseFloat(metadata.wfreq)

    // Deliverable 1: 7. Create the yticks for the bar chart.
    // Hint: Get the the top 10 otu_ids and map them in descending order 
    // so the otu_ids with the most bacteria are last. 
    var top10 = array_of_objects.sort((a,b) => b.value - a.value).slice(0,10).reverse()
    //console.log(top10)
    var topIDs = top10.map(entry => `OTU ${String(entry.id)}`)
    var topLabels = top10.map(entry => entry.label)
    var topValues = top10.map(entry => entry.value)

    var ids = array_of_objects.map(entry => entry.id)
    var labels = array_of_objects.map(entry => entry.label)
    var values = array_of_objects.map(entry => entry.value)

    // Deliverable 1: 8. Create the trace for the bar chart. 
    var barData = [{
      x: topValues,
      y: topIDs,
      type: "bar",
      orientation: "h",
      text: topLabels
    }];

    // Deliverable 1: 9. Create the layout for the bar chart. 
    var barLayout = {
    title: "Top 10 Bacteria Cultures Found"
    };

    // Deliverable 1: 10. Use Plotly to plot the data with the layout. 
    Plotly.newPlot("bar", barData, barLayout)

    // Deliverable 2: 1. Create the trace for the bubble chart.
    var bubbleData = [{
      x: ids,
      y: values,
      mode: "markers",
      marker: {
        color: ids,
        size: values
      },
      text: labels
    }]

    // Deliverable 2: 2. Create the layout for the bubble chart.
    var bubbleLayout = {
      title: "Bacteria Cultures per Sample",
      xaxis: {title: "OTU ID"},
      yaxis: {title: "Count"}
    }
    // Deliverable 2: 3. Use Plotly to plot the data with the layout.
    Plotly.newPlot("bubble", bubbleData, bubbleLayout)

    // Deliverable 3: 4. Create the trace for the gauge chart
    var gaugeData = [{
      value: wfreq,
      type: "indicator",
      mode: "gauge+number",
      title: {text: "Washing Frequency (scrubs per week)"},
      gauge: {axis: {range: [0, 10]},
        bar: {color: "black"},
        steps: [
          {range: [0,2], color: "red"},
          {range: [2,4], color: "orange"},
          {range: [4,6], color: "yellow"},
          {range: [6,8], color: "lightgreen"},
          {range: [8,10], color: "green"}
        ]
      }
    }]
    // Deliverable 3: 5. Create the layout for the gauge chart.
    // var gaugeLayout = {
    // }
    // Deliverable 3: 6. Use Plotly to plot the gauge data and layout.
    Plotly.newPlot("gauge", gaugeData)
  });
}
