function showTab(tabId, event) {
    const tabs = document.querySelectorAll('.tab');
    const buttons = document.querySelectorAll('.tab-button');

    // すべてのタブを非表示にする
    tabs.forEach(tab => tab.style.display = 'none');

    // すべてのボタンからアクティブクラスを削除
    buttons.forEach(button => button.classList.remove('active'));

    // 指定されたタブを表示
    document.getElementById(tabId).style.display = 'block';

    // アクティブなボタンにクラスを追加
    event.currentTarget.classList.add('active');
}

// 最初のタブを表示
document.addEventListener('DOMContentLoaded', function () {
    showTab('tab1', { currentTarget: document.querySelector('.tab-button') });
});