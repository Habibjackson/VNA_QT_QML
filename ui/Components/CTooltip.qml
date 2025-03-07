import QtQuick
import QtQuick.Controls.Material

ToolTip {
    id: tooltip
    property Item target

    background: Rectangle {
        id: bg
        color: "#282828" // Dark background like Spotify
        radius: 6
        opacity: 0.9
    }

    contentItem: Text {
        text: tooltip.text
        color: "white"
        font.pixelSize: 14
        wrapMode: Text.Wrap
    }

    // Animations for smooth appearance
    enter: Transition {
        NumberAnimation { property: "opacity"; from: 0; to: 1; duration: 200 }
        NumberAnimation { property: "scale"; from: 0.9; to: 1.0; duration: 200 }
    }
    exit: Transition {
        NumberAnimation { property: "opacity"; from: 1; to: 0; duration: 150 }
        NumberAnimation { property: "scale"; from: 1.0; to: 0.9; duration: 150 }
    }

    onTargetChanged: {
        if (target) {
            x = target.x + target.width + 64  // Place it on the right side
            y = target.y + (parent.height - height) / 2 // Center vertically

            // Prevent tooltip from going off the right screen edge
            // if (x + width > parent.width) {
            //     x = target.x - width - 8 // Move to the left if out of bounds
            // }
        }
    }

}
