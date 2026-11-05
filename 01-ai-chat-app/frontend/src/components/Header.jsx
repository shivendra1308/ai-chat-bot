// components/Header.jsx
import { styles } from '../styles/styles'

function Header({ onClearChat }) {
  return (
    <div style={styles.header}>
      <h1 style={styles.headerTitle}>🤖 AI Chat Assistant</h1>
      <p style={styles.headerSubtitle}>
        Powered by FastAPI + Groq
      </p>
      <button
        onClick={onClearChat}
        style={styles.clearButton}
      >
        🗑️ Clear Chat
      </button>
    </div>
  )
}

export default Header