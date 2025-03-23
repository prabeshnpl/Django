function create_button(_class, _icon)
{
   var _button = document.createElement('button');
   _button.insertAdjacentHTML('afterbegin',`<i class="${_icon}"></i>`);
   _button.classList.add(_class);
   return _button;
}

function checker(event)
{
    const checker_button = event.target.closest('button');
    const child = checker_button.querySelectorAll('i');
    let hasAppIcon = Array.from(child).some(child => 
        child.classList.contains('bi') && child.classList.contains('bi-app')
    );

    if (hasAppIcon){
        checker_button.innerHTML = '<i class = "bi bi-check"></i> ';
    }
    else {checker_button.innerHTML = '<i class = "bi bi-app"></i> ';
    }
}

function element_remover(event){

    const button_to_delete = event.target.closest('button');
    const parent = button_to_delete.parentElement;
    parent.remove();
   }

function attachRemoveButtonEvent(button)
{
    button.addEventListener('click',element_remover);
}

function attachConstantChecker(button)
{
    button.addEventListener('click',checker);
}

var inputField = document.getElementById('input_bar');
var TaskField = document.getElementById('task-field');

var input_bar_button = document.getElementById('input_bar_button');
input_bar_button.addEventListener('mouseover',function(){this.style.backgroundColor='green';});
input_bar_button.addEventListener('mouseout',function(){this.style.backgroundColor='aquamarine';});

var clear_all = document.getElementById('Clear');
clear_all.addEventListener('click',()=>{
    TaskField.innerHTML="";
})

var Remove_checked = document.getElementById('Remove_checked');
Remove_checked.addEventListener('click',()=>{
    _nodeList = TaskField.querySelectorAll('div');
    _nodeList.forEach(element => {
    const icon = element.querySelector('i');
    if (icon)
    {
        if((icon.classList.contains('bi'))&&(icon.classList.contains("bi-check"))){
            element.remove();
        }
    }
        
    });
})

var Button = document.getElementById('input_bar_button');
Button.addEventListener( 'click', function () {
    event.preventDefault();

    var newTask = inputField.value;    
    _nodeList = TaskField.querySelectorAll('div');

    if ((newTask!=='')&&(_nodeList.length<12))
    {           
        var checkbox = create_button('checkbox','bi bi-app');
        attachConstantChecker(checkbox);
        
        var _delete = create_button('_delete','bi bi-calendar-x');
        attachRemoveButtonEvent(_delete);
        
        var edit = create_button('edit','bi bi-pencil-fill');

        var texts = document.createElement('div');
        texts.classList.add('task-text');
        texts.textContent = newTask;

        var task = document.createElement('div');
        task.classList.add('task-list'); 
        task.insertAdjacentElement('afterbegin',texts);
        task.insertAdjacentElement('afterbegin',checkbox);        
        task.insertAdjacentElement('beforeend',edit);
        task.insertAdjacentElement('beforeend',_delete);
        TaskField.insertAdjacentElement('beforeend',task);
        inputField.value = '';
    }
    else if(newTask==''){
        alert('please enter task');
    }
    else{
        alert('List full')
    }
});


