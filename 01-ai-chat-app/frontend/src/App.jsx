// App.jsx
import { useState, useEffect } from 'react'
import Header from './components/Header'
import ChatWindow from './components/ChatWindow'
import InputBox from './components/InputBox'
import { chatAPI } from './services/api'
import { styles } from './styles/styles'

const USER_ID = "shivendra"

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)

  // Load history on startup
  useEffect(() => {
    loadChatHistory()
  }, [])

  const loadChatHistory = async () => {
    try {
      const data = await chatAPI.getHistory(USER_ID)
      if (data.messages.length > 0) {
        setMessages(data.messages)
      } else {
        setMessages([{
          role: "assistant",
          content: "Hi Shivendra! I am your AI assistant. How can I help you today?"
        }])
      }
    } catch (error) {
      console.error("Error loading history:", error)
    }
  }

  const sendMessage = async () => {
    if (!input.trim() || loading) return

    const userMessage = { role: "user", content: input }
    setMessages(prev => [...prev, userMessage])
    setInput("")
    setLoading(true)

    // Add empty AI message
    setMessages(prev => [...prev, {
      role: "assistant",
      content: ""
    }])

    try {
      const response = await chatAPI.sendMessage(input, USER_ID)
      const reader = response.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split('\n')

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6))
              if (data.done) {
                setLoading(false)
                break
              }
              if (data.text) {
                setMessages(prev => {
                  const updated = [...prev]
                  updated[updated.length - 1] = {
                    role: "assistant",
                    content: updated[updated.length - 1].content + data.text
                  }
                  return updated
                })
              }
            } catch (e) {}
          }
        }
      }
    } catch (error) {
      console.error("Error:", error)
    } finally {
      setLoading(false)
    }
  }

  const clearChat = async () => {
    await chatAPI.clearHistory(USER_ID)
    setMessages([{
      role: "assistant",
      content: "Chat cleared! How can I help you?"
    }])
  }

  return (
    <div style={styles.container}>
      <Header onClearChat={clearChat} />
      <ChatWindow messages={messages} loading={loading} />
      <InputBox
        input={input}
        setInput={setInput}
        onSend={sendMessage}
        loading={loading}
      />
    </div>
  )
}

export default App