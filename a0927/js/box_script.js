let num = 0;
let num2 = 0;

// 제이쿼리선언
$(function(){
  
  // 우측버튼
  $("#right").click(function(){

    if(num >= 900){
      alert("이동 불가");
      return false;
    }
    $("#box").stop();

    num += 100;
    num2 += 360;

    $("#box").animate({
      left : num, "rotate" : num2 + "deg"
    }, 1000);

  }); // 우측버튼


  // 좌측버튼
  $("#left").click(function(){
    if(num <= 0){
      alert("이동 불가");
      return false;
    }
    $("#box").stop();

    num -= 100;
    num2 -= 360;

    $("#box").animate({
      left : num, "rotate" : num2 + "deg"
    }, 1000);
  }); // 좌측버튼


}); 

