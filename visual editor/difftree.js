
function difftree(tree1, tree2){
    var diffout = "";
    var tree1Map = {};
    var tree2Map = {};
    flattenTree(tree1, tree1Map);
    flattenTree(tree2, tree2Map);
    Object.keys(tree1Map).forEach(function(parent){
        if(!tree2Map[parent]){
            diffout += "-" + parent + "\n";
            Object.keys(tree1Map[parent]).forEach(function(child){
                diffout += "-" + parent + " NT " + child + "\n";
            });
        }else{
            Object.keys(tree1Map[parent]).forEach(function(child){
                if(!tree2Map[parent][child]){
                    diffout += "-" + parent + " NT " + child + "\n";
                }
            });
        }
    });
    Object.keys(tree2Map).forEach(function(parent){
        if(!tree1Map[parent]){
            diffout += "+" + parent + "\n";
            Object.keys(tree2Map[parent]).forEach(function(child){
                diffout += "+" + parent + " NT " + child + "\n";
            });
        }else{
            Object.keys(tree2Map[parent]).forEach(function(child){
                if(!tree1Map[parent][child]){
                    diffout += "+" + parent + " NT " + child + "\n";
                }
            });
        }
    });
    return diffout;
}

function downloadString (dataStr) {
    var file = "data:text/plain;charset=utf-8,";
    var encoded = encodeURIComponent(dataStr);
    file += encoded;
    var a = document.createElement('a');
    a.href = file;
    a.target   = '_blank';
    a.download = "diffout.txt";
    document.body.appendChild(a);
    a.click();
    a.remove();
}

function flattenTree(tree, treeMap){
    if(!treeMap[tree.name]){
        treeMap[tree.name] = {};
    }
    if(tree.children){
        tree.children.forEach(function(child){
           treeMap[tree.name][child.name] = 1;
           flattenTree(child,treeMap);
        });
    }
    if(tree._children){
        tree._children.forEach(function(child){
           treeMap[tree.name][child.name] = 1;
           flattenTree(child,treeMap);
        });
    }
}
