var xmlhttp = new XMLHttpRequest();
// Query todos los contratos
var url = "http://localhost:9000/sparql?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3Fcont%20a%2Frdfs%3AsubClassOf*%20%3Chttp%3A%2F%2Fcontsem.unizar.es%2Fdef%2Fsector-publico%2Fpproc%23Contract%3E%20.%0A%7D%0A";
var dataJSON = "";

xmlhttp.onreadystatechange = function() {
	if (this.readyState == 4) {
		if (this.status == 202) {
			dataJSON = this.responseText;
            getAllContracts();
			console.log("getAllContracts");
		}
		else {
			alert("Cannot connect to the helio server");
		}
	}
};
xmlhttp.open("GET", url, true);
xmlhttp.setRequestHeader("Accept","application/sparql-results+json,*/*;q=0.9");
xmlhttp.send();

var listContractsID = [];
var infoAllContracts = [];

function getAllContracts() {
    var dataAllContracts = JSON.parse(dataJSON);

    for (key in dataAllContracts) {
        if (dataAllContracts.hasOwnProperty(key)) {
            var valueBindings = dataAllContracts[key].bindings;

            if( valueBindings ) {
                for (keyContract in valueBindings) {
                    if (valueBindings.hasOwnProperty(keyContract)) {
                        var valueId = valueBindings[keyContract].cont.value;
                        if( valueId ) {
                            listContractsID.push(valueId);
                        }
                    }
                }
            }
        }
    }

    if( listContractsID.length > 0 ) {
        var queryResult;
        listContractsID.forEach((item, index) => {
            var query = "http://localhost:9000/sparql?query=SELECT%20*%20WHERE%20%7B%0A%20%20%3C" + item + "%3E%20a%20%3FtypeOfContract%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2Fidentifier%3E%20%3Fidentifier%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fcontsem.unizar.es%2Fdef%2Fsector-publico%2Fpproc%23contractingBody%3E%20%3FcontractingBody%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fgroup01.org%2Faragon%2Fontology%2FawardedTo%3E%20%3FawardedTo%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2Fdescription%3E%20%3Fdescription%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fgroup01.org%2Faragon%2Fontology%2FhasAwardPrice%3E%20%3FhasAwardPrice%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fgroup01.org%2Faragon%2Fontology%2FhasAwardProcedure%3E%20%3FhasAwardProcedure%20.%0A%20%20%3C" + item + "%3E%20%3Chttp%3A%2F%2Fgroup01.org%2Faragon%2Fontology%2FhasBiddingPrice%3E%20%3FhasBiddingPrice%0A%7D%0A";
            var xmlhttp = new XMLHttpRequest();

            xmlhttp.onreadystatechange = function() {
            	if (this.readyState == 4) {
            		if (this.status == 202) {
            			queryResult = this.responseText;
                        addContractToList(queryResult, item.split('/Contract/')[1]);
            		}
            		else {
            			alert("Cannot connect to the helio server");
            		}
            	}
            };
            xmlhttp.open("GET", query, true);
            xmlhttp.setRequestHeader("Accept","application/sparql-results+json,*/*;q=0.9");
            xmlhttp.send();
        });
    }
}

var aux = 0;
function addContractToList(queryResult, code) {
    var infoContract = JSON.parse(queryResult);

    for (key in infoContract) {
        if (infoContract.hasOwnProperty(key)) {
            var valueBindings = infoContract[key].bindings;

            if( valueBindings ) {
                for (keyContract in valueBindings) {
                    if (valueBindings.hasOwnProperty(keyContract)) {
                        let contract = {
                            "Code": code,
                            "Company": valueBindings[keyContract].awardedTo.value,
                            "GovernmentRequester": valueBindings[keyContract].contractingBody.value,
                            "TypeOfContract": valueBindings[keyContract].typeOfContract.value,
                            "AwardProcedure": valueBindings[keyContract].hasAwardProcedure.value,
                            "BiddingPrice": valueBindings[keyContract].hasBiddingPrice.value,
                            "AwardPrice": valueBindings[keyContract].hasAwardPrice.value
                        }

                        // QUERY 2
                        var queryWikiRequest = "http://localhost:9000/sparql?query=PREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3C" + contract.Company +  "%3E%20rdfs%3Alabel%20%3Flabel%20.%0A%20%20%3C" + contract.Company +  "%3E%20owl%3AsameAs%20%3Furi%0A%7D%0A";
                        var xmlhttp = new XMLHttpRequest();

                        xmlhttp.onreadystatechange = function() {
                        	if (this.readyState == 4) {
                        		if (this.status == 202) {
                        			queryResult = this.responseText;
                        			var result = JSON.parse(queryResult);
                        			if( !isEmpty(result.results.bindings) ) {
			                        	contract.wikiCompany = result.results.bindings[0].uri.value;
			                        }
                                    // QUERY 1
                                    var queryGovRequest = "http://localhost:9000/sparql?query=PREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0ASELECT%20*%20WHERE%20%7B%0A%20%20%3C" + contract.GovernmentRequester + "%3E%20owl%3AsameAs%20%3Furi%0A%7D%0A";
                                    var xmlhttp2 = new XMLHttpRequest();

                                    xmlhttp2.onreadystatechange = function() {
                                        if (this.readyState == 4 && this.status == 202) {
                                            var queryResult2 = this.responseText;
                                            var result2 = JSON.parse(queryResult2);

                                            if( !isEmpty(result2.results.bindings) ) {
        			                        	contract.wikiGovernmentRequester = result2.results.bindings[0].uri.value;
        			                        }
                                            contract.GovernmentRequester = contract.GovernmentRequester.split("Body/")[1].replaceAll("_", " ");
                                            contract.Company = contract.Company.split("Company/")[1].replaceAll("_", " ");
                                            contract.TypeOfContract = contract.TypeOfContract.split("#")[1];
                                            infoAllContracts.push(contract);
                                        }
										aux++;

										if( aux === 99 ){
											start();
											console.log("start");
										}
                                    }
                                    xmlhttp2.open("GET", queryGovRequest, true);
                                    xmlhttp2.setRequestHeader("Accept","application/sparql-results+json,*/*;q=0.9");
                                    xmlhttp2.send();
                        		}
                        		else {
                        			alert("Cannot connect to the helio server");
                        		}
                        	}
                        };
                        xmlhttp.open("GET", queryWikiRequest, true);
                        xmlhttp.setRequestHeader("Accept","application/sparql-results+json,*/*;q=0.9");
                        xmlhttp.send();
                    }
                }
            }
        }
    }
}

String.prototype.replaceAll = function(str1, str2, ignore)
{
    return this.replace(new RegExp(str1.replace(/([\/\,\!\\\^\$\{\}\[\]\(\)\.\*\+\?\|\<\>\-\&])/g,"\\$&"),(ignore?"gi":"g")),(typeof(str2)=="string")?str2.replace(/\$/g,"$$$$"):str2);
}

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

var listItemString = $('#listItem').html();
function start() {
	infoAllContracts.forEach(buildNewList);
	$('#listItem').remove();

	/* Get unique list of elements */
	var lookupGovernmentRequester = {};
	var lookupAwardProcedure = {};
	var lookupTypeOfContract = {};
	var lookupCompany = {};

	var listGovernmentRequester = [];
	var listAwardProcedure = [];
	var listTypeOfContract = [];
	var listCompany = [];

	for (var item, i = 0; item = infoAllContracts[i++];) {
		var gov      = item.GovernmentRequester;
		var award    = item.AwardProcedure;
		var contract = item.TypeOfContract;
		var company  = item.Company;

		if (!(gov in lookupGovernmentRequester)) {
			lookupGovernmentRequester[gov] = 1;
			listGovernmentRequester.push(gov);
		}
		if (!(award in lookupAwardProcedure)) {
			lookupAwardProcedure[award] = 1;
			listAwardProcedure.push(award);
		}
		if (!(contract in lookupTypeOfContract)) {
			lookupTypeOfContract[contract] = 1;
			listTypeOfContract.push(contract);
		}
		if (!(company in lookupCompany)) {
			lookupCompany[company] = 1;
			listCompany.push(company);
		}
	}

	listGovernmentRequester.forEach(addFilterGov);
	listAwardProcedure.forEach(addFilterAward);
	listTypeOfContract.forEach(addFilterContract);
	listCompany.forEach(addFilterCompany);
}

function addFilterGov(item, index) {
	var html = "<li>" +
	'<input class="filter" data-filter=".' + item.replace(/\s/g, "")+ '" type="checkbox" id="' + item.replace(/\s/g, "") + '">' +
	'<label class="checkbox-label" for="' + item.replace(/\s/g, "") + '">' + item + '</label>' +
	"</li>";
	$('#filter-GovernmentRequester').append(html);
}

function addFilterAward(item, index) {
	var html = "<li>" +
	'<input class="filter" data-filter=".' + item.replace(/\s/g, "") + '" type="checkbox" id="' + item + '">' +
	'<label class="checkbox-label" for="' + item.replace(/\s/g, "") + '">' + item + '</label>' +
	"</li>";
	$('#filter-AwardProcedure').append(html);
}

function addFilterContract(item, index) {
	var html = '<li class="filter" data-filter=".' + item.replace(/\s/g, "") + '"><a href="#0" data-type="' + item + '">' +
	item + '</a></li>';
	$('#filter-TypeOfContract').append(html);
}

function addFilterCompany(item, index) {
	var html = "<li>" +
	'<input class="filter" data-filter=".' + item.replace(/\s/g, "") + '" type="checkbox" id="' + item + '">' +
	'<label class="checkbox-label" for="' + item.replace(/\s/g, "") + '">' + item + '</label>' +
	"</li>";
	$('#filter-Company').append(html);
}

function buildNewList(item, index) {
	var cssItem = "mix " +
	item.Code.replace(/\s/g, "") + " " +
	item.GovernmentRequester.replace(/\s/g, "") + " " +
	item.AwardProcedure.replace(/\s/g, "") + " " +
	item.TypeOfContract.replace(/\s/g, "") + " " +
	item.Company.replace(/\s/g, "");
	var listItem = $('<li class="' + cssItem + '">' + listItemString + '</li>');

	var listItemCode = $('.code', listItem);
	listItemCode.html(item.Code);
	var listItemDescription = $('.description', listItem);
	listItemDescription.html(item.Description);
	var listItemGovernmentRequester = $('.governmentRequester', listItem);
	var govItem = item.GovernmentRequester;
	if( item.wikiGovernmentRequester ) {
		govItem = "<a href=" + item.wikiGovernmentRequester + ' target="_blank">' + item.GovernmentRequester + "</a>";
	}
	listItemGovernmentRequester.html(govItem);
	var listItemAwardProcedure = $('.awardProcedure', listItem);
	listItemAwardProcedure.html(item.AwardProcedure);
	var listItemTypeOfContract = $('.typeOfContract', listItem);
	listItemTypeOfContract.html(item.TypeOfContract);
	var listItemBiddingPrice = $('.biddingPrice', listItem);
	listItemBiddingPrice.html(item.BiddingPrice + ' €');
	var listItemAwardPrice = $('.awardPrice', listItem);
	listItemAwardPrice.html(item.AwardPrice + ' €');
	var listItemCompany = $('.company', listItem);
	var companyItem = item.Company;
	if( item.wikiCompany ) {
		companyItem = "<a href=" + item.wikiCompany + ' target="_blank">' + item.Company + "</a>";
	}
	listItemCompany.html(companyItem);
	$('#dataList').append(listItem);
}

jQuery(document).ready(function($){
	//open/close lateral filter
	$('.cd-filter-trigger').on('click', function(){
		triggerFilter(true);
	});
	$('.cd-filter .cd-close').on('click', function(){
		triggerFilter(false);
	});

	function triggerFilter($bool) {
		var elementsToTrigger = $([$('.cd-filter-trigger'), $('.cd-filter'), $('.cd-tab-filter'), $('.cd-gallery')]);
		elementsToTrigger.each(function(){
			$(this).toggleClass('filter-is-visible', $bool);
		});
	}

	//mobile version - detect click event on filters tab
	var filter_tab_placeholder = $('.cd-tab-filter .placeholder a'),
		filter_tab_placeholder_default_value = 'Select',
		filter_tab_placeholder_text = filter_tab_placeholder.text();

	$('.cd-tab-filter li').on('click', function(event){
		//detect which tab filter item was selected
		var selected_filter = $(event.target).data('type');

		//check if user has clicked the placeholder item
		if( $(event.target).is(filter_tab_placeholder) ) {
			(filter_tab_placeholder_default_value == filter_tab_placeholder.text()) ? filter_tab_placeholder.text(filter_tab_placeholder_text) : filter_tab_placeholder.text(filter_tab_placeholder_default_value) ;
			$('.cd-tab-filter').toggleClass('is-open');

		//check if user has clicked a filter already selected
		} else if( filter_tab_placeholder.data('type') == selected_filter ) {
			filter_tab_placeholder.text($(event.target).text());
			$('.cd-tab-filter').removeClass('is-open');

		} else {
			//close the dropdown and change placeholder text/data-type value
			$('.cd-tab-filter').removeClass('is-open');
			filter_tab_placeholder.text($(event.target).text()).data('type', selected_filter);
			filter_tab_placeholder_text = $(event.target).text();

			//add class selected to the selected filter item
			$('.cd-tab-filter .selected').removeClass('selected');
			$(event.target).addClass('selected');
		}
	});

	//close filter dropdown inside lateral .cd-filter
	$('.cd-filter-block h4').on('click', function(){
		$(this).toggleClass('closed').siblings('.cd-filter-content').slideToggle(300);
	})

	//fix lateral filter and gallery on scrolling
	$(window).on('scroll', function(){
		(!window.requestAnimationFrame) ? fixGallery() : window.requestAnimationFrame(fixGallery);
	});

	function fixGallery() {
		var offsetTop = $('.cd-main-content').offset().top,
			scrollTop = $(window).scrollTop();
		( scrollTop >= offsetTop ) ? $('.cd-main-content').addClass('is-fixed') : $('.cd-main-content').removeClass('is-fixed');
	}

	/************************************
		MitItUp filter settings
		More details:
		https://mixitup.kunkalabs.com/
		or:
		http://codepen.io/patrickkunka/
	*************************************/

	buttonFilter.init();
	$('.cd-gallery ul').mixItUp({
	    controls: {
	    	enable: false
	    },
	    callbacks: {
	    	onMixStart: function(){
	    		$('.cd-fail-message').fadeOut(200);
	    	},
	      	onMixFail: function(){
	      		$('.cd-fail-message').fadeIn(200);
	    	}
	    }
	});

	//search filtering
	//credits http://codepen.io/edprats/pen/pzAdg
	var inputText;
	var $matching = $();

	var delay = (function(){
		var timer = 0;
		return function(callback, ms){
			clearTimeout (timer);
		    timer = setTimeout(callback, ms);
		};
	})();

	$(".cd-filter-content input[type='search']").keyup(function(){
	  	// Delay function invoked to make sure user stopped typing
	  	delay(function(){
	    	inputText = $(".cd-filter-content input[type='search']").val().toLowerCase();
	   		// Check to see if input field is empty
	    	if ((inputText.length) > 0) {
	      		$('.mix').each(function() {
		        	var $this = $(this);

		        	// add item to be filtered out if input text matches items inside the title
		        	if($this.attr('class').toLowerCase().match(inputText)) {
		          		$matching = $matching.add(this);
		        	} else {
		          		// removes any previously matched item
		          		$matching = $matching.not(this);
		        	}
	      		});
	      		$('.cd-gallery ul').mixItUp('filter', $matching);
	    	} else {
	      		// resets the filter to show all item if input is empty
	      		$('.cd-gallery ul').mixItUp('filter', 'all');
	    	}
	  	}, 200 );
	});
});

/*****************************************************
	MixItUp - Define a single object literal
	to contain all filter custom functionality
*****************************************************/
var buttonFilter = {
  	// Declare any variables we will need as properties of the object
  	$filters: null,
  	groups: [],
  	outputArray: [],
  	outputString: '',

  	// The "init" method will run on document ready and cache any jQuery objects we will need.
  	init: function(){
    	var self = this; // As a best practice, in each method we will asign "this" to the variable "self" so that it remains scope-agnostic. We will use it to refer to the parent "buttonFilter" object so that we can share methods and properties between all parts of the object.

    	self.$filters = $('.cd-main-content');
    	self.$container = $('.cd-gallery ul');

	    self.$filters.find('.cd-filters').each(function(){
	      	var $this = $(this);

		    self.groups.push({
		        $inputs: $this.find('.filter'),
		        active: '',
		        tracker: false
		    });
	    });

	    self.bindHandlers();
  	},

  	// The "bindHandlers" method will listen for whenever a button is clicked.
  	bindHandlers: function(){
    	var self = this;

    	self.$filters.on('click', 'a', function(e){
	      	self.parseFilters();
    	});
	    self.$filters.on('change', function(){
	      self.parseFilters();
	    });
  	},

  	parseFilters: function(){
	    var self = this;

	    // loop through each filter group and grap the active filter from each one.
	    for(var i = 0, group; group = self.groups[i]; i++){
	    	group.active = [];
	    	group.$inputs.each(function(){
	    		var $this = $(this);
	    		if($this.is('input[type="radio"]') || $this.is('input[type="checkbox"]')) {
	    			if($this.is(':checked') ) {
	    				group.active.push($this.attr('data-filter'));
	    			}
	    		} else if($this.is('select')){
	    			group.active.push($this.val());
	    		} else if( $this.find('.selected').length > 0 ) {
	    			group.active.push($this.attr('data-filter'));
	    		}
	    	});
	    }
	    self.concatenate();
  	},

  	concatenate: function(){
    	var self = this;

    	self.outputString = ''; // Reset output string

	    for(var i = 0, group; group = self.groups[i]; i++){
	      	self.outputString += group.active;
	    }

	    // If the output string is empty, show all rather than none:
	    !self.outputString.length && (self.outputString = 'all');

    	// Send the output string to MixItUp via the 'filter' method:
		if(self.$container.mixItUp('isLoaded')){
	    	self.$container.mixItUp('filter', self.outputString);
		}
  	}
};
