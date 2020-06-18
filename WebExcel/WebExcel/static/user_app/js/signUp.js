function submit_click(){
    var pw = document.getElementById('signupPw').value
    var pwcheck = document.getElementById('signupPwcheck').value
    if(pw == pwcheck){
        document.getElementById('signup-form').submit();
    }else{
        alert("비밀번호가 일치하지 않습니다.")
        document.getElementById('signupPwcheck').focus()
    }
}