// styles/styles.js
export const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    height: "100vh",
    maxWidth: "800px",
    margin: "0 auto",
    padding: "20px",
    background: "#ffffff",
  },
  header: {
    textAlign: "center",
    padding: "20px 0",
    borderBottom: "1px solid #e0e0e0",
    marginBottom: "20px"
  },
  headerTitle: {
    fontSize: "24px",
    fontWeight: "bold",
    color: "#000000"
  },
  headerSubtitle: {
    fontSize: "14px",
    color: "#666666",
    marginTop: "5px"
  },
  clearButton: {
    marginTop: "10px",
    padding: "8px 16px",
    borderRadius: "8px",
    border: "1px solid #e0e0e0",
    background: "transparent",
    color: "#666666",
    cursor: "pointer",
    fontSize: "13px"
  },
  chatWindow: {
    flex: 1,
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "15px",
    paddingBottom: "20px"
  },
  messageBubble: {
    maxWidth: "70%",
    padding: "12px 16px",
    borderRadius: "12px",
    display: "flex",
    flexDirection: "column",
    gap: "5px"
  },
  roleLabel: {
    fontSize: "12px",
    color: "#666666",
    fontWeight: "bold"
  },
  messageContent: {
    fontSize: "15px",
    lineHeight: "1.5",
    color: "#000000",
    whiteSpace: "pre-wrap"
  },
  inputContainer: {
    display: "flex",
    gap: "10px",
    padding: "20px 0",
    borderTop: "1px solid #e0e0e0"
  },
  input: {
    flex: 1,
    padding: "12px 16px",
    borderRadius: "8px",
    border: "1px solid #e0e0e0",
    background: "#f5f5f5",
    color: "#000000",
    fontSize: "15px",
    outline: "none"
  },
  button: {
    padding: "12px 24px",
    borderRadius: "8px",
    border: "none",
    background: "#2563eb",
    color: "#ffffff",
    fontSize: "15px",
    fontWeight: "bold",
    cursor: "pointer"
  }
}