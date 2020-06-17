$(document).ready(function(){
    $('.restaurantListDiv>li').click(function(){
        if ($(this).hasClass('active')){
            $(this).addClass('deactive')
            $(this).removeClass('active')
            $(this).next('ul').slideUp();
        }else{
            $(this).removeClass('deactive')
            $(this).addClass('active')
            $(this).next('ul').slideDown();
        }

        
    })
});

function emailCheckForm(){
    var isCheckLessThanOne = true
    for(i = 1; i <= 6; i++){
        var idString = "check"+i
        var isChecked = $("#"+idString).is(':checked')
        console.log("check"+i,isChecked)
        if (isChecked){
            isCheckLessThanOne = false
            break
        }
    }
    console.log(isCheckLessThanOne)
    if($('#inputReceiver').val().length <= 0){
        alert("이메일 수신자를 1명 이상 입력해주세요.")
        $('#inputReceiver').focus()
        return false
    }else if($('#inputTitle').val().length <= 0){
        alert("이메일 제목을 입력해주세요.")
        $('#inputTitle').focus()
        return false
    }else if(isCheckLessThanOne){
        alert("맛집을 하나 이상 선택해주세요.")
        return false
    }else{
        return true;
    }
}