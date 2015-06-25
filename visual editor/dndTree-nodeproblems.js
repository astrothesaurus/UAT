//READ MORE HERE:  http://www.robschmuecker.com/d3-js-drag-and-drop-zoomable-tree/comment-page-1/#comments


/*

    debugout.js
    by @inorganik
    
*/

// save all the console.logs
function debugout() {
    var self = this;

    // OPTIONS
    self.realTimeLoggingOn = true; // log in real time (forwards to console.log)
    self.useTimestamps = false; // insert a timestamp in front of each log
    self.useLocalStorage = false; // store the output using window.localStorage() and continuously add to the same log each session
    self.recordLogs = true; // set to false after you're done debugging to avoid the log eating up memory
    self.autoTrim = true; // to avoid the log eating up potentially endless memory
    self.maxLines = 2500; // if autoTrim is true, this many most recent lines are saved
    self.tailNumLines = 100; // how many lines tail() will retrieve
    self.logFilename = 'uat-changes.json'; // filename of log downloaded with downloadLog()

    // vars
    self.depth = 0;
    self.parentSizes = [0];
    self.currentResult = '';
    self.startTime = new Date();
    self.output = '';

    this.version = function() { return '0.5.0' }

    /*
        USER METHODS
    */  
    this.getLog = function() {
        var retrievalTime = new Date();
        // if recording is off, so dev knows why they don't have any logs
        if (!self.recordLogs) {
            self.log('[debugout.js] log recording is off.');
        }
        // if using local storage, get values
        if (self.useLocalStorage) {
            var saved = window.localStorage.getItem('debugout.js');
            if (saved) {
                saved = JSON.parse(saved);
                self.startTime = new Date(saved.startTime);
                self.output = saved.log;
                retrievalTime = new Date(saved.lastLog);
            }
        }
        return self.output
            //+ '\n---- Log retrieved: '+retrievalTime+' ----\n'
            //+ self.formatSessionDuration(self.startTime, retrievalTime);
    }
    // accepts optional number or uses the default for number of lines
    this.tail = function(numLines) {
        var numLines = numLines || self.tailLines;
        return self.trimLog(self.getLog(), numLines);
    }
    // accepts a string to search for
    this.search = function(string) {
        var lines = self.output.split('\n');
        var rgx = new RegExp(string);
        var matched = [];
        // can't use a simple Array.prototype.filter() here
        // because we need to add the line number
        for (var i = 0; i < lines.length; i++) {
            var addr = '['+i+'] ';
            if (lines[i].match(rgx)) {
                matched.push(addr + lines[i]);
            }
        }
        var result = matched.join('\n');
        if (result.length == 0) result = 'Nothing found for "'+string+'".';
        return result
    }
    // accepts the starting line and how many lines after the starting line you want
    this.getSlice = function(lineNumber, numLines) {
        var lines = self.output.split('\n');
        var segment = lines.slice(lineNumber, lineNumber + numLines);
        return segment.join('\n');
    }
    // immediately downloads the log - for desktop browser use
    this.downloadLog = function() {
        var file = "data:text/plain;charset=utf-8,";
        var logFile = self.getLog();
        var encoded = encodeURIComponent(logFile);
        file += encoded;
        var a = document.createElement('a');
        a.href = file;
        a.target   = '_blank';
        a.download = self.logFilename;
        document.body.appendChild(a);
        a.click();
        a.remove();
    }
    // clears the log
    this.clear = function() {
        var clearTime = new Date();
        self.output = ''//'---- Log cleared: '+clearTime+' ----\n';
        if (self.useLocalStorage) {
            // local storage
            var saveObject = {
                startTime: self.startTime,
                log: self.output,
                lastLog: clearTime
            }
            saveObject = JSON.stringify(saveObject);
            window.localStorage.setItem('debugout.js', saveObject);
        }
        if (self.realTimeLoggingOn) console.log('[debugout.js] clear()');
    }
    // records a log
    this.log = function(obj) {
        // log in real time
        if (self.realTimeLoggingOn) console.log(obj);
        // record log
        var type = self.determineType(obj);
        if (type != null && self.recordLogs) {
            var addition = self.formatType(type, obj);
            // timestamp, formatted for brevity
            if (self.useTimestamps) {
                var logTime = new Date();
                self.output += self.formatTimestamp(logTime);
            }
            self.output += addition+'\n';
            if (self.autoTrim) self.output = self.trimLog(self.output, self.maxLines);
            // local storage
            if (self.useLocalStorage) {
                var last = new Date();
                var saveObject = {
                    startTime: self.startTime,
                    log: self.output,
                    lastLog: last
                }
                saveObject = JSON.stringify(saveObject);
                window.localStorage.setItem('debugout.js', saveObject);
            }
        }
        self.depth = 0;
        self.parentSizes = [0];
        self.currentResult = '';
    }
    /*
        METHODS FOR CONSTRUCTING THE LOG
    */

    // like typeof but classifies objects of type 'object'
    // kept separate from formatType() so you can use at your convenience!
    this.determineType = function(object) {
        if (object != null) {
            var typeResult;
            var type = typeof object;
            if (type == 'object') {
                var len = object.length;
                if (len == null) {
                    if (typeof object.getTime == 'function') {
                        typeResult = 'Date';
                    }
                    else if (typeof object.test == 'function') {
                        typeResult = 'RegExp';
                    }
                    else {
                        typeResult = 'Object';
                    }
                } else {
                    typeResult = 'Array';
                }
            } else {
                typeResult = type;
            }
            return typeResult;
        } else {
            return null;
        }
    }
    // format type accordingly, recursively if necessary
    this.formatType = function(type, obj) {
        switch(type) {
            case 'Object' :
                self.currentResult += '{\n';
                self.depth++;
                self.parentSizes.push(self.objectSize(obj));
                var i = 0;
                for (var prop in obj) {
                    self.currentResult += self.indentsForDepth(self.depth);
                    self.currentResult += prop + ': ';
                    var subtype = self.determineType(obj[prop]);
                    var subresult = self.formatType(subtype, obj[prop]);
                    if (subresult) {
                        self.currentResult += subresult;
                        if (i != self.parentSizes[self.depth]-1) self.currentResult += ',';
                        self.currentResult += '\n';
                    } else {
                        if (i != self.parentSizes[self.depth]-1) self.currentResult += ',';
                        self.currentResult += '\n';
                    }
                    i++;
                }
                self.depth--;
                self.parentSizes.pop();
                self.currentResult += self.indentsForDepth(self.depth);
                self.currentResult += '}';
                if (self.depth == 0) return self.currentResult;
                break;
            case 'Array' :
                self.currentResult += '[';
                self.depth++;
                self.parentSizes.push(obj.length);
                for (var i = 0; i < obj.length; i++) {
                    var subtype = self.determineType(obj[i]);
                    if (subtype == 'Object' || subtype == 'Array') self.currentResult += '\n' + self.indentsForDepth(self.depth);
                    var subresult = self.formatType(subtype, obj[i]);
                    if (subresult) {
                        self.currentResult += subresult;
                        if (i != self.parentSizes[self.depth]-1) self.currentResult += ', ';
                        if (subtype == 'Array') self.currentResult += '\n';
                    } else {
                        if (i != self.parentSizes[self.depth]-1) self.currentResult += ', ';
                        if (subtype != 'Object') self.currentResult += '\n';
                        else if (i == self.parentSizes[self.depth]-1) self.currentResult += '\n';
                    }
                }
                self.depth--;
                self.parentSizes.pop();
                self.currentResult += ']';
                if (self.depth == 0) return self.currentResult;
                break;
            case 'function' :
                obj += '';
                var lines = obj.split('\n');
                for (var i = 0; i < lines.length; i++) {
                    if (lines[i].match(/\}/)) self.depth--;
                    self.currentResult += self.indentsForDepth(self.depth);
                    if (lines[i].match(/\{/)) self.depth++;
                    self.currentResult += lines[i] + '\n';
                }
                return self.currentResult;
                break;
            case 'RegExp' :
                return '/'+obj.source+'/';
                break;
            case 'Date' :
            case 'string' : 
                if (self.depth > 0 || obj.length == 0) {
                    return '"'+obj+'"';
                } else {
                    return obj;
                }
            case 'boolean' :
                if (obj) return 'true';
                else return 'false';
            case 'number' :
                return obj+'';
                break;
        }
    }
    this.indentsForDepth = function(depth) {
        var str = '';
        for (var i = 0; i < depth; i++) {
            str += '\t';
        }
        return str;
    }
    this.trimLog = function(log, maxLines) {
        var lines = log.split('\n');
        if (lines.length > maxLines) {
            lines = lines.slice(lines.length - maxLines);
        }
        return lines.join('\n');
    }
    this.lines = function() {
        return self.output.split('\n').length;
    }
    // calculate testing time
    this.formatSessionDuration = function(startTime, endTime) {
        var msec = endTime - startTime;
        var hh = Math.floor(msec / 1000 / 60 / 60);
        var hrs = ('0' + hh).slice(-2);
        msec -= hh * 1000 * 60 * 60;
        var mm = Math.floor(msec / 1000 / 60);
        var mins = ('0' + mm).slice(-2);
        msec -= mm * 1000 * 60;
        var ss = Math.floor(msec / 1000);
        var secs = ('0' + ss).slice(-2);
        msec -= ss * 1000;
        return '---- Session duration: '+hrs+':'+mins+':'+secs+' ----'
    }
    this.formatTimestamp = function(timestamp) {
        var year = timestamp.getFullYear();
        var date = timestamp.getDate();
        var month = ('0' + (timestamp.getMonth() +1)).slice(-2);
        var hrs = Number(timestamp.getHours()); 
        var mins = ('0' + timestamp.getMinutes()).slice(-2);
        var secs = ('0' + timestamp.getSeconds()).slice(-2);
        return '['+ year + '-' + month + '-' + date + ' ' + hrs + ':' + mins + ':'+secs + ']: ';
    }
    this.objectSize = function(obj) {
        var size = 0, key;
        for (key in obj) {
            if (obj.hasOwnProperty(key)) size++;
        }
        return size;
    }

    /*
        START/RESUME LOG
    */
    if (self.useLocalStorage) {
        var saved = window.localStorage.getItem('debugout.js');
        if (saved) {
            saved = JSON.parse(saved);
            self.output = saved.log;
            var start = new Date(saved.startTime);
            var end = new Date(saved.lastLog);
            self.output += '\n---- Session end: '+saved.lastLog+' ----\n';
            self.output += self.formatSessionDuration(start, end);
            self.output += '\n\n';
        }
    } 
    self.output += '---- Session started: '+self.startTime+' ----\n\n';
}


//READ MORE HERE:  http://www.robschmuecker.com/d3-js-drag-and-drop-zoomable-tree/comment-page-1/#comments

// Get JSON data


var uat = "uat.json"
var astronomicalobjects = "astronomical_objects.json"
var astrophysicalmagnetism = "astrophysical_magnetism.json"
var celestialmechanics = "celestial_mechanics.json"
var cosmology = "cosmology.json"
var equipmentandapparatus = "equipment_and_apparatus.json"
var galacticphysics = "galactic_physics.json"
var interdisciplinaryastronomy = "interdisciplinary_astronomy.json"
var lunarphysics = "lunar_physics.json"
var methodsandtechniques = "methods_and_techniques.json"
var nuclearastrophysics = "nuclear_astrophysics.json"
var observationalastronomy = "observational_astronomy.json"
var planetaryscience = "planetary_science.json"
var positionalastronomy = "positional_astronomy.json"
var spaceexploration = "space_exploration.json"
var stellarphysics = "stellar_physics.json"



function renderTree(j){
treeJSON = d3.json(j, function(error, treeData) {
    var treeDataExtend = {};
    var orphans = {};
    orphans["name"] = "orphans";
    orphans["children"] = [];
    orphans["_children"] = [];
    treeDataExtend["name"] = "root";
    treeDataExtend["children"] = [orphans, treeData];
    treeData = treeDataExtend;
    // Calculate total nodes, max label length
    var totalNodes = 0;
    var maxLabelLength = 0;
    // variables for drag/drop
    var selectedNode = null;
    var draggingNode = null;
    // panning variables
    var panSpeed = 200;
    var panBoundary = 20; // Within 20px from edges will pan when dragging.
    // Misc. variables
    var i = 0;
    var duration = 750;
    var root;
    var orig;

    // size of the diagram
    var viewerWidth = $(document).width();
    var viewerHeight = $(document).height();
    var tree = d3.layout.tree()
        .size([viewerHeight, viewerWidth]);

    // define a d3 diagonal projection for use by the node paths later on.
    var diagonal = d3.svg.diagonal()
        .projection(function(d) {
            return [d.y, d.x];
        });

    // A recursive helper function for performing some setup by walking through all nodes

    function visit(parent, visitFn, childrenFn) {
        if (!parent) return;

        visitFn(parent);

        var children = childrenFn(parent);
        if (children) {
            var count = children.length;
            for (var i = 0; i < count; i++) {
                visit(children[i], visitFn, childrenFn);
            }
        }
    }

    // Call visit function to establish maxLabelLength
    visit(treeData, function(d) {
        totalNodes++;
        maxLabelLength = Math.max(d.name.length, maxLabelLength);

    }, function(d) {
        return d.children && d.children.length > 0 ? d.children : null;
    });


    // sort the tree according to the node names

    function sortTree() {
        tree.sort(function(a, b) {
            return b.name.toLowerCase() < a.name.toLowerCase() ? 1 : -1;
        });
    }
    // Sort the tree initially incase the JSON isn't in a sorted order.
    sortTree();

    // TODO: Pan function, can be better implemented.

    function pan(domNode, direction) {
        var speed = panSpeed;
        if (panTimer) {
            clearTimeout(panTimer);
            translateCoords = d3.transform(svgGroup.attr("transform"));
            if (direction == 'left' || direction == 'right') {
                translateX = direction == 'left' ? translateCoords.translate[0] + speed : translateCoords.translate[0] - speed;
                translateY = translateCoords.translate[1];
            } else if (direction == 'up' || direction == 'down') {
                translateX = translateCoords.translate[0];
                translateY = direction == 'up' ? translateCoords.translate[1] + speed : translateCoords.translate[1] - speed;
            }
            scaleX = translateCoords.scale[0];
            scaleY = translateCoords.scale[1];
            scale = zoomListener.scale();
            svgGroup.transition().attr("transform", "translate(" + translateX + "," + translateY + ")scale(" + scale + ")");
            d3.select(domNode).select('g.node').attr("transform", "translate(" + translateX + "," + translateY + ")");
            zoomListener.scale(zoomListener.scale());
            zoomListener.translate([translateX, translateY]);
            panTimer = setTimeout(function() {
                pan(domNode, speed, direction);
            }, 50);
        }
    }

    // Define the zoom function for the zoomable tree

    function zoom() {
        svgGroup.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
    }


    // define the zoomListener which calls the zoom function on the "zoom" event constrained within the scaleExtents
    var zoomListener = d3.behavior.zoom().scaleExtent([0.1, 3]).on("zoom", zoom);

    function initiateDrag(d, domNode) {
        draggingNode = d;
        d3.select(domNode).select('.ghostCircle').attr('pointer-events', 'none');
        d3.selectAll('.ghostCircle').attr('class', 'ghostCircle show');
        d3.select(domNode).attr('class', 'node activeDrag');

        svgGroup.selectAll("g.node").sort(function(a, b) { // select the parent and sort the path's
            if (a.id != draggingNode.id) return 1; // a is not the hovered element, send "a" to the back
            else return -1; // a is the hovered element, bring "a" to the front
        });
        // if nodes has children, remove the links and nodes
        if (nodes.length > 1) {
            // remove link paths
            links = tree.links(nodes);
            nodePaths = svgGroup.selectAll("path.link")
                .data(links, function(d) {
                    return d.target.id;
                }).remove();
            // remove child nodes
            nodesExit = svgGroup.selectAll("g.node")
                .data(nodes, function(d) {
                    return d.id;
                }).filter(function(d, i) {
                    if (d.id == draggingNode.id) {
                        return false;
                    }
                    return true;
                }).remove();
        }

        // remove parent link
        parentLink = tree.links(tree.nodes(draggingNode.parent));
        svgGroup.selectAll('path.link').filter(function(d, i) {
            if (d.target.id == draggingNode.id) {
                return true;
            }
            return false;
        }).remove();

        dragStarted = null;
    }

    // define the baseSvg, attaching a class for styling and the zoomListener
    var baseSvg = d3.select("#tree-container").html("").append("svg")
        .attr("width", viewerWidth-20)
        .attr("height", viewerHeight-70)
        .attr("class", "overlay")
        .call(zoomListener);


    // Define the drag listeners for drag/drop behaviour of nodes.
    dragListener = d3.behavior.drag()
        .on("dragstart", function(d) {
            if (d == root) {
                return;
            }
            dragStarted = true;
            nodes = tree.nodes(d);
            d3.event.sourceEvent.stopPropagation();
            // it's important that we suppress the mouseover event on the node being dragged. Otherwise it will absorb the mouseover event and the underlying node will not detect it d3.select(this).attr('pointer-events', 'none');
        })
        .on("drag", function(d) {
            if(d.name == "orphans"){
                return;
            }
            if (d == root) {
                return;
            }
            if (dragStarted) {
                domNode = this;
                initiateDrag(d, domNode);
            }

            // get coords of mouseEvent relative to svg container to allow for panning
            relCoords = d3.mouse($('svg').get(0));
            if (relCoords[0] < panBoundary) {
                panTimer = true;
                pan(this, 'left');
            } else if (relCoords[0] > ($('svg').width() - panBoundary)) {

                panTimer = true;
                pan(this, 'right');
            } else if (relCoords[1] < panBoundary) {
                panTimer = true;
                pan(this, 'up');
            } else if (relCoords[1] > ($('svg').height() - panBoundary)) {
                panTimer = true;
                pan(this, 'down');
            } else {
                try {
                    clearTimeout(panTimer);
                } catch (e) {

                }
            }

            d.x0 += d3.event.dy;
            d.y0 += d3.event.dx;
            var node = d3.select(this);
            node.attr("transform", "translate(" + d.y0 + "," + d.x0 + ")");
            updateTempConnector();
        }).on("dragend", function(d) {
            if (d == root) {
                return;
            }
            domNode = this;
            if (selectedNode) {
                // now remove the element from the parent, and insert it into the new elements children
                var index = draggingNode.parent.children.indexOf(draggingNode);
                if (index > -1) {
                    draggingNode.parent.children.splice(index, 1);
                }
                if (typeof selectedNode.children !== 'undefined' || typeof selectedNode._children !== 'undefined') {
                    if (typeof selectedNode.children !== 'undefined') {
                        selectedNode.children.push(draggingNode);
                    } else {
                        selectedNode._children.push(draggingNode);
                    }
                } else {
                    selectedNode.children = [];
                    selectedNode.children.push(draggingNode);
                }
                // Make sure that the node being added to is expanded so user can see added node is correctly moved
                expand(selectedNode);
                //collapse(selectedNode.children);
                sortTree();
                endDrag();
            } else {
                endDrag();
            }
        });

    function endDrag() {
        selectedNode = null;
        d3.selectAll('.ghostCircle').attr('class', 'ghostCircle');
        d3.select(domNode).attr('class', 'node');
        // now restore the mouseover event or we won't be able to drag a 2nd time
        d3.select(domNode).select('.ghostCircle').attr('pointer-events', '');
        updateTempConnector();
        if (draggingNode !== null) {
            collapse(draggingNode); //< --- collapse the node in question at all times when dropped.
            update(root);
            centerNode(draggingNode);
            draggingNode = null;
            }
        }


    // Helper functions for collapsing and expanding nodes.

    function collapse(d) {
        if (d.children) {
            d._children = d.children;
            d._children.forEach(collapse);
            d.children = null;
        }
    }

    function expand(d) {
        if (d._children) {
            d.children = d._children;
            //d.children.forEach(expand); //possible comment out?
            d._children = null;
        }
    }

    var overCircle = function(d) {
        selectedNode = d;
        updateTempConnector();
    };
    var outCircle = function(d) {
        selectedNode = null;
        updateTempConnector();
    };

    // Function to update the temporary connector indicating dragging affiliation
    var updateTempConnector = function() {
        var data = [];
        if (draggingNode !== null && selectedNode !== null) {
            // have to flip the source coordinates since we did this for the existing connectors on the original tree
            data = [{
                source: {
                    x: selectedNode.y0,
                    y: selectedNode.x0
                },
                target: {
                    x: draggingNode.y0,
                    y: draggingNode.x0
                }
            }];
        }
        var link = svgGroup.selectAll(".templink").data(data);

        link.enter().append("path")
            .attr("class", "templink")
            .attr("d", d3.svg.diagonal())
            .attr('pointer-events', 'none');

        link.attr("d", d3.svg.diagonal());

        link.exit().remove();
    };

    // Function to center node when clicked/dropped so node doesn't get lost when collapsing/moving with large amount of children.

    function centerNode(source) {
        scale = zoomListener.scale();
        x = -source.y0;
        y = -source.x0;
        x = x * scale + viewerWidth / 2;
        y = y * scale + viewerHeight / 2;
        d3.select('g').transition()
            .duration(duration)
            .attr("transform", "translate(" + x + "," + y + ")scale(" + scale + ")");
        zoomListener.scale(scale);
        zoomListener.translate([x, y]);
    }

    // Toggle children function

    function toggleChildren(d) {
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else if (d._children) {
            d.children = d._children;
            d._children = null;
        }
        return d;
    }

    // Toggle children on click.

    function click(d) {
        if (d3.event.defaultPrevented) return; // click suppressed
        d = toggleChildren(d);
        update(d);
        centerNode(d);
    }

    function update(source) {
        // Compute the new height, function counts total children of root node and sets tree height accordingly.
        // This prevents the layout looking squashed when new nodes are made visible or looking sparse when nodes are removed
        // This makes the layout more consistent.
        var levelWidth = [1];
        var childCount = function(level, n) {

            if (n.children && n.children.length > 0) {
                if (levelWidth.length <= level + 1) levelWidth.push(0);

                levelWidth[level + 1] += n.children.length;
                n.children.forEach(function(d) {
                    childCount(level + 1, d);
                });
            }
        };
        childCount(0, root);
        var newHeight = d3.max(levelWidth) * 45; // 25 pixels per line  
        tree = tree.size([newHeight, viewerWidth]);

        // Compute the new tree layout.
        var nodes = tree.nodes(root).reverse(),
            links = tree.links(nodes);

        // Set widths between levels based on maxLabelLength.
        nodes.forEach(function(d) {
            d.y = (d.depth * (maxLabelLength * 5)); //maxLabelLength * 10px
            // alternatively to keep a fixed scale one can set a fixed depth per level
            // Normalize for fixed-depth by commenting out below line
            // d.y = (d.depth * 500); //500px per level.
        });

        // Update the nodes…
        node = svgGroup.selectAll("g.node")
            .data(nodes, function(d) {
                return d.id || (d.id = ++i);
            });

        // Enter any new nodes at the parent's previous position.
        var nodeEnter = node.enter().append("g")
            .call(dragListener)
            .attr("class", "node")
            .attr("transform", function(d) {
                return "translate(" + source.y0 + "," + source.x0 + ")";
            })
            .on('click', click);

        nodeEnter.append("circle")
            .attr('class', 'nodeCircle')
            .attr("r", 0)
            .style("fill", function(d) {
                return d._children ? "lightsteelblue" : "#fff";
            });

        nodeEnter.append("text")
            .attr("x", function(d) {
                return d.children || d._children ? -10 : 10;
            })
            .attr("dy", ".35em")
            .attr('class', 'nodeText')
            .attr("text-anchor", function(d) {
                return d.children || d._children ? "end" : "start";
            })
            .text(function(d) {
                return d.name;
            })
            .style("fill-opacity", 0);

        // phantom node to give us mouseover in a radius around it
        nodeEnter.append("circle")
            .attr('class', 'ghostCircle')
            .attr("r", 30)
            .attr("opacity", 0.2) // change this to zero to hide the target area
        .style("fill", "red")
            .attr('pointer-events', 'mouseover')
            .on("mouseover", function(node) {
                overCircle(node);
            })
            .on("mouseout", function(node) {
                outCircle(node);
            });

        // Update the text to reflect whether node has children or not.
        node.select('text')
            .attr("x", function(d) {
                return d.children || d._children ? -10 : 10;
            })
            .attr("text-anchor", function(d) {
                return d.children || d._children ? "end" : "start";
            })
            .text(function(d) {
                return d.name;
            });

        // Change the circle fill depending on whether it has children and is collapsed
        node.select("circle.nodeCircle")
            .attr("r", 4.5)
            .style("fill", function(d) {
                return d._children ? "lightsteelblue" : "#fff";
            });

        // Transition nodes to their new position.
        var nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function(d) {
                return "translate(" + d.y + "," + d.x + ")";
            });

        // Fade the text in
        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        var nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function(d) {
                return "translate(" + source.y + "," + source.x + ")";
            })
            .remove();

        nodeExit.select("circle")
            .attr("r", 0);

        nodeExit.select("text")
            .style("fill-opacity", 0);

        // Update the links…
        var link = svgGroup.selectAll("path.link")
            .data(links, function(d) {
                return d.target.id;
            });

        // Enter any new links at the parent's previous position.
        link.enter().insert("path", "g")
            .attr("class", "link")
            .attr("d", function(d) {
                var o = {
                    x: source.x0,
                    y: source.y0
                };
                return diagonal({
                    source: o,
                    target: o
                });
            });

        // Transition links to their new position.
        link.transition()
            .duration(duration)
            .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
            .duration(duration)
            .attr("d", function(d) {
                var o = {
                    x: source.x,
                    y: source.y
                };
                return diagonal({
                    source: o,
                    target: o
                });
            })
            .remove();

        // Stash the old positions for transition.
        nodes.forEach(function(d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });

        //sanitizedNodes = returnSanitized(root);
        //console.log(sanitizedNodes);
        //console.log(JSON.stringify(sanitizedNodes));
    }

    // Append a group which holds all nodes and which the zoom Listener can act upon.
    var svgGroup = baseSvg.append("g");

    // Define the root
    root = treeData;
    orig=JSON.parse(JSON.stringify(treeData));
    root.x0 = viewerHeight / 2;
    root.y0 = 0;

    // Collapse all children of roots children before rendering.
    root.children.forEach(function(child){
    collapse(child);
    });

    // Layout the tree initially and center on the root node.
    update(root);
    centerNode(root);
    expand(orphans);
function fullexpand(d) {
     //console.log("initial val of expand d", d)
        if (d._children) {
            d.children = d._children;
            d.children.forEach(fullexpand);
            d._children = null;
        }
    };

function fullcollapse(d) {
    //console.log("initial val of collapse d", d)
        if (d.children) {
            d._children = d.children;
            d._children.forEach(fullcollapse);
            d.children = null;
        }
    };

addNode = function(nodeName){
    var newNode = {};
    newNode["name"] = nodeName;
    newNode.children = [];
    orphans.children.push(newNode);
    update(root);
}

getRoot = function(){
    return root;
};

getOrig = function(){
    return orig;
};

finalize = function final2() {
    bugout.clear();
    collapse(root);
    fullexpand(root);
    sanitizedNodes = returnSanitized(root);
    bugout.log(JSON.stringify(sanitizedNodes));
    fullcollapse(root);
    expand(root);
    update(root);
    //centerNode(root);
    };

function returnSanitized(node) {
    var sanNode = {};
    sanNode.name = node.name;
    sanNode.children = [];
    if (node.children) {
        node.children.forEach(function (child, index, array) {
            sanNode.children.push(returnSanitized(child));
        });
    }
    return sanNode;
}

})};


// generate initial legend
//renderTree(uat);

// handle on click event
d3.select('#opts')
  .on('change', function() {
    var newData = eval(d3.select(this).property('value'));
    renderTree(newData);
});

