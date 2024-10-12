    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    const squareSize = 20;  // Size of each square in the drawing
    const color = 'black';  // Color for the squares

    function drawSquare(x, y, size) {
        ctx.fillStyle = color;
        ctx.fillRect(x, y, size, size);
    }

    function drawText(message, x, y) {
        let offsetX = x;

        for (let i = 0; i < message.length; i++) {
            const letter = message[i];
            switch (letter) {
                case 'a':
                    drawA(offsetX, y);
                    break;
                case 'b':
                    drawB(offsetX, y);
                    break;
                case 'c':
                    drawC(offsetX, y);
                    break;
                case 'd':
                    drawD(offsetX, y);
                    break;
                case 'e':
                    drawE(offsetX, y);
                    break;
                case 'f':
                    drawF(offsetX, y);
                    break;
                case 'g':
                    drawG(offsetX, y);
                    break;
                case 'i':
                    drawI(offsetX, y);
                    break;
                case 'j':
                    drawJ(offsetX, y);
                    break;
                case ' ':
                    offsetX += squareSize;  // Space is a simple offset
                    break;
            }
            offsetX += squareSize * 2;  // Add a gap between letters
        }
    }

    function drawA(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x + squareSize, y, squareSize);
        drawSquare(x + squareSize * 2, y, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize * 2, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 2, squareSize);
        drawSquare(x + squareSize, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize, squareSize);
    }

    function drawB(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize * 3, squareSize);
        drawSquare(x, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize, y, squareSize);
        drawSquare(x + squareSize, y - squareSize, squareSize);
        drawSquare(x + squareSize, y - squareSize * 3, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 2, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 3, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize * 3, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize * 4, squareSize);
    }

    function drawC(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize * 3, squareSize);
        drawSquare(x, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 4, squareSize);
    }

    function drawD(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize * 3, squareSize);
        drawSquare(x, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 3, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize * 2, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize, squareSize);
        drawSquare(x + squareSize * 2, y, squareSize);
    }

    function drawE(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x + squareSize, y, squareSize);
        drawSquare(x + squareSize * 2, y, squareSize);
        drawSquare(x + squareSize * 3, y, squareSize);
        drawSquare(x + squareSize * 3, y - squareSize, squareSize);
        drawSquare(x + squareSize * 2, y - squareSize * 2, squareSize);
        drawSquare(x + squareSize, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x - squareSize, y, squareSize);
        drawSquare(x - squareSize, y - squareSize, squareSize);
        drawSquare(x - squareSize, y - squareSize * 2, squareSize);
    }

    function drawF(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
        drawSquare(x, y - squareSize * 3, squareSize);
        drawSquare(x, y - squareSize * 4, squareSize);
        drawSquare(x + squareSize, y, squareSize);
        drawSquare(x + squareSize * 2, y, squareSize);
    }

    function drawG(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x - squareSize, y, squareSize);
        drawSquare(x + squareSize, y, squareSize);
        drawSquare(x + squareSize * 2, y, squareSize);
        drawSquare(x + squareSize * 3, y, squareSize);
        drawSquare(x + squareSize * 3, y + squareSize, squareSize);
        drawSquare(x + squareSize * 3, y + squareSize * 2, squareSize);
        drawSquare(x + squareSize * 3, y + squareSize * 3, squareSize);
        drawSquare(x + squareSize * 3, y + squareSize * 4, squareSize);
    }

    function drawI(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y + squareSize, squareSize);
        drawSquare(x, y + squareSize * 2, squareSize);
        drawSquare(x, y + squareSize * 3, squareSize);
        drawSquare(x, y + squareSize * 5, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
    }

    function drawJ(x, y) {
        drawSquare(x, y, squareSize);
        drawSquare(x, y + squareSize, squareSize);
        drawSquare(x, y + squareSize * 2, squareSize);
        drawSquare(x, y + squareSize * 3, squareSize);
        drawSquare(x, y + squareSize * 5, squareSize);
        drawSquare(x, y - squareSize, squareSize);
        drawSquare(x, y - squareSize * 2, squareSize);
        drawSquare(x - squareSize, y - squareSize * 3, squareSize);
    }

    // Example usage:
    drawText('abcde', 50, 100);
