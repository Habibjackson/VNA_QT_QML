// Paper.qml
import QtQuick

Item {
    id: paper

    // Custom properties for the paper component
    property color color: theme.paperBackground // Background color of the paper
    property real radius: 5 // Corner radius
    property real shadowRadius: 10 // Shadow blur radius
    property color shadowColor: "#80000000" // Shadow color
    property real shadowVerticalOffset: 2 // Vertical offset of the shadow
    property real shadowHorizontalOffset: 2 // Horizontal offset of the shadow

    // Shadow rectangle
    Rectangle {
        id: shadowRect
        anchors.fill: parent
        color: paper.shadowColor
        radius: paper.radius + paper.shadowRadius
        opacity: 0.5
        z: -1 // Place it behind the paper
        anchors {
            leftMargin: paper.shadowHorizontalOffset
            topMargin: paper.shadowVerticalOffset
        }
    }

    // The main rectangle representing the paper
    Rectangle {
        id: paperRect
        color: paper.color
        radius: paper.radius
        anchors.fill: parent
    }
}
