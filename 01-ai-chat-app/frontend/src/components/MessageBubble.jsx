// components/MessageBubble.jsx
import { styles } from '../styles/styles'

function MessageBubble({ message, isLoading, isLast }) {
  const isUser = message.role === "user"

  return (
    <div
      style={{
        ...styles.messageBubble,
        alignSelf: isUser ? "flex-end" : "flex-start",
        background: isUser ? "#2563eb" : "#f0f0f0",
      }}
    >
      <span style={{
        ...styles.roleLabel,
        color: isUser ? "#ffffff" : "#666666"
      }}>
        {isUser ? "👤 You" : "🤖 AI"}
      </span>
      <p style={{
        ...styles.messageContent,
        color: isUser ? "#ffffff" : "#000000"
      }}>
        {message.content || (isLoading && isLast ? "▋" : "")}
      </p>
    </div>
  )
}

export default MessageBubble  // ← This line missing!