

/**************** home page methods ***************/

// display last 12 cards 
var display_cards = function(latest_entries){

    $.each(latest_entries, function(i,entry){

        var valid_review = ""

        $.each(entry.reviews, function(i,r){
            if (r.mark_as_deleted == false){
                valid_review = "Review: ' " + r.review.substring(0,100) + "...' Click on the image to see more!"
            }
        })

        var card = $("<div class='card'></div>")

        var image = $("<img class='card-img-top card-image' src='" + entry.img  + "' alt='Card " + entry.name + " food image'>")
        $(image).click(function(){
            window.location.href =  '/view/' + entry.id
        })
        
        var card_body = $("<div class='card-body'><h5 class='card-title'>" + entry.name + "</h5><p class='card-text'> State: "+ entry.state + "<br> Rating: "+ entry.rating + "</p> <p class='card-text'><small class='text-muted'>"+ valid_review +"</small></p></div>")

        var full_card = card.append(image).append(card_body)

        if (i < 4 ){
            $('.card-group#cards-1').append(
                full_card
            );
        }
        else if (i < 8){
            $('.card-group#cards-2').append(
                full_card
            );
        }
        else{
            $('.card-group#cards-3').append(
                full_card
            );
        }
    });
}

/**************** search results page methods ***************/

// display results 
var display_query_results = function(query_results){

    num_results = query_results.length

    if (num_results == 0){
        $('#num-search-results').html("0 matches found for '" + query_1 + "'")
    }
    else{

        $('#num-search-results').html( num_results + " matches found for '" + query_1 + "'")
        
        // apply gestalt principles 
        span_beg = "<span class='highlight'>"
        span_end = "</span>" 

        $.each(query_results, function(i,entry){

            name = entry.name
            state = entry.state
            about = entry.about 
           
            position = 0  
            $.each(state.match(new RegExp(query_1, 'gi')), function(i,word){
                position = state.indexOf(word, position)
                state = state.substring(0, position) +  span_beg + word + span_end + state.substring(position + word.length, state.length)
                position = position + span_beg.length + span_end.length
            });
            
            position = 0 
            $.each(name.match(new RegExp(query_1, 'gi')), function(i,word){
                position = name.indexOf(word, position)
                name = name.substring(0, position) +  span_beg + word + span_end + name.substring(position + word.length, name.length)
                position = position + span_beg.length + span_end.length
            });
           
            position = 0  
            $.each(about.match(new RegExp(query_1, 'gi')), function(i,word){
                position = about.indexOf(word, position)
                about = about.substring(0, position) +  span_beg + word + span_end + about.substring(position + word.length, about.length)
                position = position + span_beg.length + span_end.length
            });
        
            // display cards 
            var card = $("<div class='card card-results' '><div class='row no-gutters'><div class='col-md-4'><img class='card-img results-img' src='" + entry.img  + "' alt='Card "+ entry.name +" image'></div><div class='col-md-8'><div class='card-body'><h5 class='card-title'>" + name + "</h5><p class='card-text'> State: "+ state + "<br> Rating: "+ entry.rating + "</p> <p class='card-text'><small class='text-muted'>"+ about +"</small></p></div></div></div></div>")

            $(card).click(function(){
                window.location.href =  '/view/' + entry.id
            })

            $('#search-results').append(card)
        });
    }
}

// search a query 
var search_query = function(query){
    window.location.href =  '/search_query/' + query  
}

/**************** create page methods ***************/

// helps to display error messages to correct location 
function error(error_div,input, msg, addClass){
    $(error_div).html(msg);
    $(input).focus();

    if (addClass == true){
        $(input).addClass("warning-input-border")
    }
    else{
        $(input).removeClass("warning-input-border")
    }
}

// validates if a string is a number between 0 - 5 
function isValidRating(value){

    if (isNaN(value)){
        return false; 
    }
    else{
        if (parseInt(value) < 0  || parseInt(value) > 5){
            return false
        }
        else{
            return true
        }
    }
}

function isNotEmpty(value){
    if (value.trim().length == 0){
        return false
    }
    else{
        return true
    }
}

function isValidImg(value){
    if( value.substr( value.length - 4 ) == ".jpg" || value.substr( value.length - 4 ) == ".png" || value.substr( value.length - 5 ) == ".jpeg" ){
        return true
    }
    else{
        return false
    }
}

function create_entry(name, img, about, state, location, review, rating){
    $('#new-entry-verification').empty()

    new_data = { 'name' : name, 'img':img, 'about':about, 'state':state, 'location':location, 'review':review, 'rating': rating}
    
    $.ajax({
        type: "POST",
        url: "create",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(new_data),
        success: function(result){
            $('#new-entry-verification').append(" New Item Successfully Created. <a href=/view/"+ result['new_id'] +">  Click Here! </a>")
            $("#input-name").val('');
            $("#input-img").val('');
            $("#input-about").val('');
            $("#input-state").val('');
            $("#input-location").val('');
            $("#input-review").val('');
            $("#input-rating").val('');
        },
        error: function(request, status, error){
            $('#new-entry-verification').html("Error:" + error)
        }
    });

}
/**************** view page methods ***************/
function display_view(food_truck_data){
    
    /* Display information */
    $('.truck-name').html(food_truck_data.name)
    $('.view-img').append($("<img class='food-img' src= " + food_truck_data.img + " alt= '"  + food_truck_data.name +" food image'>")) 
    $('.important-info').append($("<div class='vertical-center'> State: " + food_truck_data.state + "</div> <div class='vertical-center'> Rating: " + food_truck_data.rating + "</div>"))
    $('.about-info').append($("<div class='vertical-center about-title-section'>  About: </div>"))
    $('.about-info').append($("<div class='vertical-center about-info'>" + food_truck_data.about + "</div>"))
}

function display_location_view(food_truck_data){
    /* location edit attribute */
    var edit_icon = $("<i class='far fa-edit icon'></i>")
    $(edit_icon).click(function(){
        $('.location-info').empty()
        edit_location(food_truck_data)
    })
    var location = $("<div class='view-location'>" + "<i class='fas fa-map-marker-alt'></i> &nbsp" +  food_truck_data.location + "&nbsp &nbsp &nbsp</div>").append(edit_icon)
    $('.location-info').append(location)
}

function edit_location(food_truck_data){

    var input = $("<label for='location-edit'>Location:&nbsp&nbsp</label><input type='text' id='location-edit' value='"+ food_truck_data.location +"' autofocus ><br>")
    
    var submit_button = $("<button type='button' class='btn btn-success btn-suc'>Submit</button>")
    
    $(submit_button).click(function(){
        var location_data = $("#location-edit").val();
        update_location(location_data, food_truck_data.id)
    })
    
    var discard_button = $("<button type='button' class='btn btn-warning btn-warn'> Discard Changes </button>")
    $(discard_button).click(function(){
        window.location.href =  '/view/' + food_truck_data.id
    })

    $('.location-info').append(input)
    $('.location-info').append(submit_button)
    $('.location-info').append(discard_button)

}

function update_location(location, id){
    data_to_add = {'location':location, 'id':id}
    $.ajax({
        type: "POST",
        url: "update_location",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_add),
        success: function(result){
            window.location.href =  '/view/' + result['truck_id']
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function display_review_view(food_truck_data){
    var comment_button = $("<button type='button' class='btn btn-secondary review-button'> ADD REVIEW &nbsp <i class='far fa-comment-alt'></i></button>")
    $(comment_button).click(function(){
        $('.add-comment').empty()
        edit_review(food_truck_data)
    })
    
    $('.add-comment').append(comment_button)

    $.each(food_truck_data.reviews , function(i,r){
        if (r.mark_as_deleted == false){
            var row = $("<div class='row vertical-center' id=' " + i + "'></div>")
            var comment = $("<div class='col-md-11 review'> '" + r.review  + "' </div>")
            var remove_button = $("<button type='button' class='comment-remove-btn'> X </button>")

            $(remove_button).click(function(){
                remove_comment(row, food_truck_data.id, i)
                update_comment(food_truck_data.id, i, true)
            })

            var comment_row = row.append(comment).append(remove_button)
            $('.reviews').append(comment_row)
        }
        
    })

}

function remove_comment(row,food_truck_id, i){
    $(row).empty()
    var undo_button = $("<button type='button' class='btn btn-warning btn-undo'> Undo Delete </button>")
    $(undo_button).click(function(){
        update_comment(food_truck_id,i,false)
        window.location.href =  '/view/' + food_truck_data.id
    })
    $(row).append(undo_button)

}

function update_comment(truck_id, comment_id,delete_comment){
    data_to_update = {'truck_id':truck_id, 'comment_id':comment_id, 'delete_comment':delete_comment}
    $.ajax({
        type: "POST",
        url: "update_comment",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_update),
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function edit_review(food_truck_data){

    var input = $("<label for='new-review'>New Review:&nbsp&nbsp</label><input type='text' id='new-review' autofocus ><br>")
    
    var submit_button = $("<button type='button' class='btn btn-success btn-suc'>Submit</button>")
    
    $(submit_button).click(function(){
        var review = $("#new-review").val();
        update_review(review, food_truck_data.id)
    })
    
    var discard_button = $("<button type='button' class='btn btn-warning btn-warn'> Discard Changes </button>")
    $(discard_button).click(function(){
        window.location.href =  '/view/' + food_truck_data.id
    })

    $('.add-comment').append(input)
    $('.add-comment').append(submit_button)
    $('.add-comment').append(discard_button)

}

function update_review(review, id){
    data_to_add = {'review':review, 'id':id}
    $.ajax({
        type: "POST",
        url: "update_review",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_add),
        success: function(result){
            window.location.href =  '/view/' + result['truck_id']
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}



/**************** load document ***************/
$(document).ready(function(){


    $("#search-button").click(function(event){
        event.preventDefault();
        var query = $("#search-input").val();
        search_query(query)
    });

    if(window.location.pathname == '/'){
        display_cards(latest_entries)
    }

    if(window.location.pathname == '/create'){
        $("#submit-button").click(function(event) {

            var name = $("#input-name").val();
            var img = $("#input-img").val();
            var about = $("#input-about").val();
            var state = $("#input-state").val();
            var location = $("#input-location").val();
            var review = $("#input-review").val();
            var rating = $("#input-rating").val();

            error("#rating-warning", "#input-rating", " ", false);
            error("#review-warning","#input-review", " ", false);
            error("#location-warning", "#input-location", " ", false);
            error("#state-warning","#input-state", " ", false);
            error("#about-warning", "#input-about", " ", false);
            error("#img-warning","#input-img", " ", false);
            error("#name-warning", "#input-name", " ", false);

            if ( !isNotEmpty(name)  || !isNotEmpty(img) || !isValidImg(img) || !isNotEmpty(about) || !isNotEmpty(state) || !isNotEmpty(location) || !isNotEmpty(review) || !isNotEmpty(rating) || !isValidRating(rating) ){
                if (!isNotEmpty(rating) || !isValidRating(rating)){
                    error("#rating-warning","#input-rating", "ERROR: Input a valid number between 0-5.", true);
                }
                if (!isNotEmpty(review)){
                    error("#review-warning", "#input-review", "ERROR: Missing Review", true);
                }
                if (!isNotEmpty(location)){
                    error("#location-warning","#input-location", "ERROR: Missing Address", true);
                }
                if (!isNotEmpty(state)){
                    error("#state-warning", "#input-state", "ERROR: Missing State", true);
                }
                if (!isNotEmpty(about)){
                    error("#about-warning","#input-about", "ERROR: Missing About", true);
                }
                if (!isNotEmpty(img) || !isValidImg(img)){
                    error("#img-warning", "#input-img", "ERROR: Enter a valid .jpg, .jpeg, .png file", true);
                }
                if (!isNotEmpty(name)){
                    error("#name-warning","#input-name", "ERROR: Missing Food Truck Name", true);
                }
            }
            else{
                create_entry(name, img, about, state, location, review, rating)
            }
            
        });
    }

    if(window.location.pathname.search(/search_query/) > -1 ){
        display_query_results(query_results)
    }

    if(window.location.pathname.search(/view/) > -1 ){
        display_view(food_truck_data)
        display_location_view(food_truck_data)
        display_review_view(food_truck_data)
    }

});