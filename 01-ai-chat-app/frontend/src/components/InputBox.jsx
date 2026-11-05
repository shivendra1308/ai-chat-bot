// components/InputBox.jsx
import { styles } from '../styles/styles'

function InputBox({ input, setInput, onSend, loading }) {

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      onSend()
    }
  }

  return (
    <div style={styles.inputContainer}>
      <input
        style={styles.input}
        type="text"
        placeholder="Type your message... (Enter to send)"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        disabled={loading}
      />
      <button
        style={{
          ...styles.button,
          opacity: loading ? 0.5 : 1
        }}
        onClick={onSend}
        disabled={loading}
      >
        {loading ? "⏳" : "Send ➤"}
      </button>
    </div>
  )
}

export default InputBox