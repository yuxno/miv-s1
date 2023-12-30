document.addEventListener('DOMContentLoaded', function () {
    const connectFour = document.getElementById('connect-four');
    const ROWS = 6;
    const COLS = 7;
    let board = Array.from({ length: ROWS }, () => Array(COLS).fill(null));
    let currentPlayer = 'red';

    // Create game board
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.row = row;
        cell.dataset.col = col;
        cell.addEventListener('click', handleCellClick);
        connectFour.appendChild(cell);
      }
    }
  
    function handleCellClick(event) {
      const { row, col } = event.target.dataset;
      const emptyRow = findEmptyRow(parseInt(col));
      
      if (emptyRow !== -1) {
        board[emptyRow][col] = currentPlayer;
        updateBoard();
        if (checkForWin(emptyRow, col)) {
          alert(`Player ${currentPlayer.toUpperCase()} wins!`);
          resetGame();
        } else if (checkForDraw()) {
          alert('It\'s a draw!');
          resetGame();
        } else {
          currentPlayer = currentPlayer === 'red' ? 'yellow' : 'red';
        }
      }
    }
  
    function updateBoard() {
      const cells = document.querySelectorAll('.cell');
      cells.forEach(cell => {
        const { row, col } = cell.dataset;
        const piece = board[row][col];
        cell.className = `cell ${piece || ''}`;
      });
    }
  
    function findEmptyRow(col) {
      for (let row = ROWS - 1; row >= 0; row--) {
        if (!board[row][col]) {
          return row;
        }
      }
      return -1; // Column is full
    }
  
    function checkForWin(row, col) {
      // Implement your logic to check for a win
      // You may check horizontally, vertically, and diagonally
      return false;
    }
  
    function checkForDraw() {
      // Implement your logic to check for a draw
      // Check if all cells are filled
      return board.every(row => row.every(cell => cell));
    }
  
    function resetGame() {
      board = Array.from({ length: ROWS }, () => Array(COLS).fill(null));
      currentPlayer = 'red';
      updateBoard();
    }
  });
  