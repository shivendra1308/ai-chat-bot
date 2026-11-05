// components/ChatWindow.jsx
import { useRef, useEffect } from 'react'
import MessageBubble from './MessageBubble'
import { styles } from '../styles/styles'

function ChatWindow({ messages, loading }) {
  const messagesEndRef = useRef(null)

  // Auto scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    })
  }, [messages])

  return (
    <div style={styles.chatWindow}>
      {messages.length === 0 && (
        <div style={{
          textAlign: "center",
          color: "#888",
          padding: "20px"
        }}>
          Loading chat history... ⏳
        </div>
      )}

      {messages.map((msg, index) => (
        <MessageBubble
          key={index}
          message={msg}
          isLoading={loading}
          isLast={index === messages.length - 1}
        />
      ))}

      <div ref={messagesEndRef} />
    </div>
  )
}

export default ChatWindow