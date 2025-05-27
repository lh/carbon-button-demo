import React, { useEffect } from "react"
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"

interface State {
  numClicks: number
  isDarkMode: boolean
}

class CarbonButton extends StreamlitComponentBase<State> {
  public state = { numClicks: 0, isDarkMode: false }

  public componentDidMount() {
    // Add global styles for SVG icons
    const style = document.createElement('style')
    style.textContent = `
      .carbon-button-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 16px;
        height: 16px;
        flex-shrink: 0;
      }
      .carbon-button-icon svg {
        width: 100%;
        height: 100%;
        fill: currentColor;
      }
      .carbon-button-content {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        width: 100%;
      }
      .carbon-button-icon-only {
        padding: 0.75rem !important;
      }
    `
    document.head.appendChild(style)
    
    // Check for dark mode
    const checkDarkMode = () => {
      const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      this.setState({ isDarkMode: isDark })
    }
    
    // Initial check
    checkDarkMode()
    
    // Listen for changes
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', checkDarkMode)
    }
  }
  
  public componentWillUnmount() {
    // Clean up listener
    if (window.matchMedia) {
      const checkDarkMode = () => {
        const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
        this.setState({ isDarkMode: isDark })
      }
      window.matchMedia('(prefers-color-scheme: dark)').removeEventListener('change', checkDarkMode)
    }
  }

  public render = (): React.ReactNode => {
    const { label, icon, buttonType, disabled, useContainerWidth, colors } = this.props.args
    
    // Debug: Log what we're receiving
    console.log("Carbon Button Debug:", { 
      label, 
      hasIcon: !!icon,
      iconLength: icon?.length,
      iconPreview: icon?.substring(0, 100), 
      buttonType,
      allArgs: this.props.args 
    })
    
    // Extra debug - check if icon contains SVG
    if (icon) {
      console.log("Icon contains <svg>:", icon.includes('<svg'))
      console.log("Icon contains viewBox:", icon.includes('viewBox'))
    }
    
    const hasIcon = icon && icon.trim() !== ''
    const hasLabel = label && label.trim() !== ''
    const isIconOnly = hasIcon && !hasLabel

    // Adjust padding for visual balance
    // When icon + text: more padding on right to balance the visual weight
    // When icon only: equal padding
    let padding = "0.75rem 1rem"
    if (isIconOnly) {
      padding = "0.75rem"
    } else if (hasIcon && hasLabel) {
      // Asymmetric padding: less on left (icon side), more on right
      padding = "0.75rem 1.25rem 0.75rem 0.875rem"
    }

    const buttonStyle: React.CSSProperties = {
      backgroundColor: this.getBackgroundColor(buttonType),
      color: this.getTextColor(buttonType),
      border: buttonType === "ghost" ? `1px solid ${this.getBorderColor(buttonType)}` : buttonType === "secondary" ? `1px solid ${this.getBorderColor(buttonType)}` : "none",
      padding: padding,
      fontSize: "14px",
      fontWeight: 400,
      borderRadius: 0,
      cursor: disabled ? "not-allowed" : "pointer",
      display: "inline-flex",
      alignItems: "center",
      justifyContent: "center",
      width: useContainerWidth ? "100%" : "auto",
      transition: "all 70ms cubic-bezier(0.2, 0, 0.38, 0.9)",
      fontFamily: '"IBM Plex Sans", system-ui, -apple-system, sans-serif',
      lineHeight: 1,
      opacity: disabled ? 0.5 : 1,
      boxShadow: buttonType === "secondary" ? "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.05)" : "none",
      outline: "none",
    }

    return (
      <button
        style={buttonStyle}
        className={isIconOnly ? "carbon-button-icon-only" : ""}
        onClick={this.onClicked}
        disabled={disabled}
        onMouseEnter={(e) => this.handleHover(e, true)}
        onMouseLeave={(e) => this.handleHover(e, false)}
        onMouseDown={this.handleMouseDown}
        onMouseUp={this.handleMouseUp}
      >
        <div className="carbon-button-content">
          {hasIcon && (
            <span 
              className="carbon-button-icon"
              dangerouslySetInnerHTML={{ __html: icon }} 
            />
          )}
          {hasLabel && <span>{label}</span>}
        </div>
      </button>
    )
  }

  private getBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_bg && type === "secondary") {
      return this.props.args.colors.rest_bg
    }
    
    // Different colors for light/dark mode
    const lightColors: { [key: string]: string } = {
      primary: "#0f62fe",
      secondary: "#e6e2e2",  // Your custom light mode color
      danger: "#da1e28",
      ghost: "transparent",
    }
    
    const darkColors: { [key: string]: string } = {
      primary: "#0f62fe",
      secondary: "#ecdcdc",  // Your custom dark mode color
      danger: "#da1e28",
      ghost: "transparent",
    }
    
    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_text && type === "secondary") {
      return this.props.args.colors.rest_text
    }
    
    const colors: { [key: string]: string } = {
      primary: "#ffffff",
      secondary: "#1a1a1a",  // Almost black for maximum contrast
      danger: "#ffffff",
      ghost: "#262626",
    }
    return colors[type] || colors.primary
  }

  private getBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.rest_border && type === "secondary") {
      return this.props.args.colors.rest_border
    }
    
    const lightColors: { [key: string]: string } = {
      primary: "#0f62fe",
      secondary: "#cccccc",
      danger: "#da1e28",
      ghost: "transparent",
    }
    
    const darkColors: { [key: string]: string } = {
      primary: "#0f62fe",
      secondary: "#404040",  // Your dark mode border
      danger: "#da1e28",
      ghost: "transparent",
    }
    
    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }

  private getHoverBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_bg && type === "secondary") {
      return this.props.args.colors.hover_bg
    }
    
    const lightColors: { [key: string]: string } = {
      primary: "#0043ce",
      secondary: "#f5f5f5",  // Light mode hover
      danger: "#ba1b23",
      ghost: "#e0e0e0",
    }
    
    const darkColors: { [key: string]: string } = {
      primary: "#0043ce",
      secondary: "#f6f4f4",  // Dark mode hover
      danger: "#ba1b23",
      ghost: "#e0e0e0",
    }
    
    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }
  
  private getHoverTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_text && type === "secondary") {
      return this.props.args.colors.hover_text
    }
    
    return this.getTextColor(type)
  }
  
  private getHoverBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.hover_border && type === "secondary") {
      return this.props.args.colors.hover_border
    }
    
    return this.getBorderColor(type)
  }
  
  private getActiveBackgroundColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_bg && type === "secondary") {
      return this.props.args.colors.active_bg
    }
    
    const lightColors: { [key: string]: string } = {
      primary: "#002d9c",
      secondary: "#50e4e0",  // Light mode teal
      danger: "#750e13",
      ghost: "#c0c0c0",
    }
    
    const darkColors: { [key: string]: string } = {
      primary: "#002d9c",
      secondary: "#67cccc",  // Dark mode teal
      danger: "#750e13",
      ghost: "#c0c0c0",
    }
    
    const colors = this.state.isDarkMode ? darkColors : lightColors
    return colors[type] || colors.primary
  }
  
  private getActiveTextColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_text && type === "secondary") {
      return this.props.args.colors.active_text
    }
    
    // Dark mode uses black text on teal
    if (this.state.isDarkMode && type === "secondary") {
      return "#000000"
    }
    
    // Light mode uses white text on teal
    if (!this.state.isDarkMode && type === "secondary") {
      return "#ffffff"
    }
    
    return this.getTextColor(type)
  }
  
  private getActiveBorderColor = (type: string): string => {
    // Use custom colors if provided
    if (this.props.args.colors?.active_border && type === "secondary") {
      return this.props.args.colors.active_border
    }
    
    return this.getBorderColor(type)
  }

  private handleHover = (e: React.MouseEvent<HTMLButtonElement>, isHover: boolean) => {
    const button = e.currentTarget
    const type = this.props.args.buttonType || "primary"
    
    if (isHover) {
      button.style.backgroundColor = this.getHoverBackgroundColor(type)
      button.style.color = this.getHoverTextColor(type)
      button.style.borderColor = this.getHoverBorderColor(type)
      button.style.transform = "translateY(-1px)"
      button.style.boxShadow = "0 2px 6px rgba(0, 0, 0, 0.15)"
    } else {
      button.style.backgroundColor = this.getBackgroundColor(type)
      button.style.color = this.getTextColor(type)
      button.style.borderColor = this.getBorderColor(type)
      button.style.transform = "translateY(0)"
      button.style.boxShadow = type === "secondary" ? "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.05)" : "none"
    }
  }
  
  private handleMouseDown = (e: React.MouseEvent<HTMLButtonElement>) => {
    const button = e.currentTarget
    const type = this.props.args.buttonType || "primary"
    
    button.style.backgroundColor = this.getActiveBackgroundColor(type)
    button.style.color = this.getActiveTextColor(type)
    button.style.borderColor = this.getActiveBorderColor(type)
    button.style.transform = "translateY(0)"
    button.style.boxShadow = "inset 0 1px 2px rgba(0, 0, 0, 0.2)"
  }
  
  private handleMouseUp = (e: React.MouseEvent<HTMLButtonElement>) => {
    // Return to hover state since mouse is still over the button
    this.handleHover(e, true)
  }

  private onClicked = (): void => {
    this.setState(
      prevState => ({ numClicks: prevState.numClicks + 1 }),
      () => Streamlit.setComponentValue(this.state.numClicks)
    )
  }
}

export default withStreamlitConnection(CarbonButton)