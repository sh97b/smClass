// 1. ajax를 사용하여 데이터 가져오기
$(function(){
  let count = 1;
  let tr_this;

  let name;
  let kor;
  let eng;
  let math;

  let total = 0;
  let avg = 0;

  let temp = 0; // 수정버튼 클릭 확인


  $.ajax({
    url : "js/stuData.json",
    type : "get",
    data : "",
    dataType : "json",


    success : function(data){

      // 데이터 가져오기
      var s_data = "";

      for(var i = 0; i < data.length; i++){
        count++;
        console.log(count);

        let korData = Number(data[i].kor);
        let engData = Number(data[i].eng);
        let mathData = Number(data[i].math);

        total = korData + engData + mathData;
        avg = ((total) / 3).toFixed(2);

        s_data += `<tr id='${(i+1)}'>`;
        s_data += `<td>${data[i].no}</td>`;
        s_data += `<td>${data[i].name}</td>`;
        s_data += `<td>${korData}</td>`;
        s_data += `<td>${engData}</td>`;
        s_data += `<td>${mathData}</td>`;
        s_data += `<td>${total}</td>`;
        s_data += `<td>${avg}</td>`;
        s_data += `<td>
                    <button class='updateBtn'>수정</button>
                    <button class='delBtn'>삭제</button>
                   </td>`;
        s_data += `</tr>`;
      }
      $("#tbody").html(s_data);
    }, 
    error : function(){
      alert("연결 실패");
    }
  }); // ajax


  // 입력버튼
  $(document).on("click", "#create", function(){

    name = $("#name").val();
    kor = Number($("#kor").val());
    eng = Number($("#eng").val());
    math = Number($("#math").val());

    total = kor + eng + math;
    avg = (total / 3);

    // 입력한 값이 들어있는지 확인
    console.log(name, kor, eng, math, total, avg);

    // 빈칸이 있는지 확인
    if(name.length < 1 || kor.length < 1|| eng.length < 1|| math.length < 1){
      alert("데이터를 입력하셔야 저장이 가능합니다.");
      return false;
    }else{
      alert("학생정보를 저장합니다.");
    }

    // 표를 만들어서 새로운 학생정보를 추가하기
    let s_data = "";

    s_data += `<tr id='${count}'>`;
    s_data += `<td>${count}</td>`;
    s_data += `<td>${name}</td>`;
    s_data += `<td>${kor}</td>`;
    s_data += `<td>${eng}</td>`;
    s_data += `<td>${math}</td>`;
    s_data += `<td>${total}</td>`;
    s_data += `<td>${avg}</td>`;
    s_data += `<td>
                <button class='updateBtn'>수정</button>
                <button class='delBtn'>삭제</button>
               </td>`;
    s_data += `</tr>`;
  
    // 맨 윗줄에 저장된 정보 출력
    $("#tbody").prepend(s_data);

    // 입력한 후 텍스트박스 초기화
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    
    count++;  // 다음번호
  }); //#create 입력버튼

  // 수정버튼
  $(document).on("click", ".updateBtn", function(){

    // 수정 버튼 클릭이 되어있는지 확인
    if(temp == 1){
      alert("수정완료 또는 수정취소 버튼을 먼저 클릭하셔야 합니다.");
      return false;
    }

    tr_this = this;
    $(this).css({"color" : "red", "font-weight" : "600"});


    alert("수정을 진행합니다.");
    count = $(this).closest("tr").attr("id");

    // 수정하려는 자리의 id 번호를 셈
    console.log(count + "번 표 수정");


    // 수정하려는 데이터를 텍스트박스에 가져오기 //
    // 수학이 마지막값이고, this의 parent의 전전전에 있음(prev 3번) 근데 이거 똑같은거 여러번쓰기 귀찮으니까 변수 만들기
    let up_data = $(this).parent().prev().prev().prev();

    name = up_data.prev().prev().prev().text();
    kor = up_data.prev().prev().text();
    eng = up_data.prev().text();
    math = up_data.text();

    console.log("이름 : " + name);
    console.log("국어 : " + kor);
    console.log("영어 : " + eng);
    console.log("수학 : " + math);

    // 입력 텍스트박스에 값 넣기
    $("#name").val(name);
    $("#kor").val(kor);
    $("#eng").val(eng);
    $("#math").val(math);

    $("#create, #update, #updateCancel").toggle();
    temp = 0;
  }); //.updateBtn 수정버튼


  // 수정완료버튼 // 이부분은 위에거랑 헷갈리니까(비슷한 걸 또 썼는데 이걸 변수나 다른 걸로 만들 수 있지 않을까) 다시 공부하자
  $(document).on("click", "#update", function(){
    tr_this.css({"color" : "black", "font-weight" : "400"});
    
    // 입력된 데이터 가져오기
    name = $("#name").val();
    kor = Number($("#kor").val());
    eng = Number($("#eng").val());
    math = Number($("#math").val());
    total = kor + eng + math;
    avg = (total/3);

    // console.log(name, kor, eng, math, total, avg); 잘 들어갔나 확인

    if(name.length < 1 || kor.length < 1 || eng.length < 1 || math.length < 1){
      alert("데이터를 입력하셔야 저장이 가능합니다.");
      return false;
    }else{
      alert("수정이 완료되었습니다.");
    }

    // 테이블의 데이터를 수정. 표 만들어서 수정하기

    // 이거 맨 처음에도 썼는데 어떻게 줄일 수 있을지 생각해보자
    let s_data = "";

    s_data += `<td>${count}</td>`;
    s_data += `<td>${name}</td>`;
    s_data += `<td>${kor}</td>`;
    s_data += `<td>${eng}</td>`;
    s_data += `<td>${math}</td>`;
    s_data += `<td>${total}</td>`;
    s_data += `<td>${avg}</td>`;
    s_data += `<td>
                <button class='updateBtn'>수정</button>
                <button class='delBtn'>삭제</button>
               </td>`;
  
    // 맨 윗줄에 저장된 정보 출력
    $("#" + count).html(s_data);

    // 수정하고 나서 텍스트박스 초기화
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#create, #update, #updateCancel").toggle();
    temp = 0;
  }); // #update 수정완료버튼

  // 수정취소버튼
  $(document).on("click", "#updateCancel", function(){
    alert("수정이 취소되었습니다.");
    tr_this.css({"color" : "black", "font-weight" : "400"});

    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#create, #update, #updateCancel").toggle();
    temp = 1;
  });

  // 삭제버튼
  $(document).on("click", ".delBtn", function(){
    count = $(this).closest("tr").attr("id");

    if(confirm("삭제하시겠습니까?")){
      $("#" + count).remove();
      alert(count + "번 학생이 삭제되었습니다.");
    }
  }); // .delBtn
}); // js